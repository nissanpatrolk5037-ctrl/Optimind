import os
import sys
import subprocess
import importlib
import re
import tempfile
from typing import Dict, List, Tuple, Optional, Any
from functools import lru_cache
from groq import Groq
import socket
import urllib.request

def _get_groq_client() -> Optional[Any]:
    if Groq is None:
        print("[ERROR] Groq library not available.")
        return None

    if not API_KEY or API_KEY == "":
        print("[ERROR] Groq API key not configured.")
        return None

    try:
        return Groq(api_key=API_KEY)
    except Exception as e:
        print(f"[ERROR] Failed to initialize Groq client: {e}")
        return None

@lru_cache(maxsize=128)
def groq_call(instructions, query) -> Optional[str]:
    client = _get_groq_client()
    if client is None:
        return "Groq client not available."

    content = instructions if query is None else f"{instructions}\n\n{query}"

    models = [
        "llama-3.3-70b-versatile",
        "llama-3.1-8b-instant",
        "meta-llama/llama-guard-4-12b"
    ]

    for model in models:
        try:
            response = client.chat.completions.create(
                model=model,
                messages=[{"role": "user", "content": content}],
                stream=False,
            )

            text = response.choices[0].message.content or ""
            return text.replace("**", "")

        except Exception as e:
            e_str = str(e)

            if re.search(r"rate limit", e_str, re.IGNORECASE):
                print(f"❌ Rate limit for {model}, switching model...")
                continue

            print(f"[Groq Error] {e_str}")
            return None

    print("⚠️ All models exhausted. Try again later.")
    return None

def check_internet_connection(timeout: int = 3) -> bool:
    """Check if internet connection is available"""
    try:
        # Try to connect to Google DNS
        socket.create_connection(("8.8.8.8", 53), timeout=timeout)
        return True
    except OSError:
        pass
    
    try:
        # Try to access a reliable website
        urllib.request.urlopen("https://www.google.com", timeout=timeout)
        return True
    except:
        pass
    
    return False

def get_llm_response(instructions, query: Optional[str] = None) -> Optional[str]:
    """
    Get LLM response from Groq (if online) or local LLM (if offline)
    """
    content = instructions if query is None else f"{instructions}\n\n{query}"
    
    # First try Groq if internet is available
    if check_internet_connection():
        print("🌐 Using Groq API (online)")
        response = groq_call(instructions, query)
        if response and len(response) > 0:
            return response.replace("**", "")
    
    # Fall back to local LLM
    print("📴 Using local LLM (offline mode)")
    try:
        # Import local LLM executor
        from local_llm_exec import get_best_local_llm_response
        
        # Determine task type for model selection
        if "code" in content.lower() or "program" in content.lower():
            task_type = "coding"
        elif "math" in content.lower() or "calculate" in content.lower():
            task_type = "math"
        elif "explain" in content.lower() or "how to" in content.lower():
            task_type = "explanation"
        else:
            task_type = "general"
        
        return get_best_local_llm_response(content, task_type)
    except ImportError as e:
        print(f"Local LLM not available: {e}")
        return "I'm currently offline and local LLM is not configured. Please check your internet connection."
    except Exception as e:
        print(f"Local LLM error: {e}")
        return "Error processing request offline."

# Import your API key
try:
    from data import API_KEY
except ImportError:
    API_KEY = os.getenv("GROQ_API_KEY", "")
    if not API_KEY:
        raise ValueError("Please set GROQ_API_KEY environment variable or create data.py with API_KEY")

client = Groq(api_key=API_KEY)

class SystemFileProtector:
    """Targeted protection against system file deletion"""
    
    # CRITICAL: System directories and files that must NEVER be deleted
    PROTECTED_SYSTEM_PATHS = {
        # Windows critical paths
        r'[Cc]:[\\/][Ww]indows[\\/][Ss]ystem32',
        r'[Cc]:[\\/][Ww]indows[\\/][Ss]ysWOW64',
        r'[Cc]:[\\/][Ww]indows[\\/][Ss]ystem',
        r'[Cc]:[\\/][Bb]oot',
        r'[Cc]:[\\/][Pp]rogram[Ff]iles',
        r'[Cc]:[\\/][Pp]rogram[Dd]ata',
        r'[Cc]:[\\/][Pp]rogram[Ff]iles \(x86\)',
        r'[Cc]:[\\/][Ww]indows[\\/]',
        r'[\\/][Ww]indows[\\/]',
        
        # Linux/Unix critical paths
        r'/(bin|sbin|usr/bin|usr/sbin|lib|usr/lib|lib64|usr/lib64|etc|boot|root|var)',
        r'/etc/passwd',
        r'/etc/shadow',
        r'/etc/sudoers',
        r'/boot/',
        r'/root/',
        r'/dev/',
        r'/proc/',
        r'/sys/',
        
        # macOS critical paths
        r'/System/',
        r'/Library/',
        r'/Applications/',
        r'/usr/bin/',
        r'/usr/sbin/',
        r'/usr/lib/',
        
        # Dangerous patterns in commands
        r'rm\s+-rf\s+/\s*',  # rm -rf /
        r'rm\s+-rf\s+/\.\.',  # rm -rf /..
        r'rm\s+-rf\s+~',  # rm -rf ~
        r'del\s+/[sS]\s+/[qQ]\s+[Cc]:\\',
        r'format\s+[Cc]:',
        r'chkdsk\s+/[fF]',
        r'dd\s+.*if=.*of=/dev/[hs]d[a-z]',
        r'mkfs\.',
        r'fdisk\s+',
        
        # Python file operations on system paths
        r'os\.remove\(.*[\\/](system32|System32|SYSWOW64|Windows)[\\/]',
        r'shutil\.rmtree\(.*[\\/](system32|System32|SYSWOW64|Windows)[\\/]',
        r'os\.unlink\(.*[\\/](system32|System32|SYSWOW64|Windows)[\\/]',
        r'open\(.*[\\/](system32|System32|Windows)[\\/].*["\']w',
    }
    
    # High-risk commands that should trigger warnings
    HIGH_RISK_COMMANDS = [
        r'subprocess\.run\(.*shell=True',
        r'os\.system\(',
        r'eval\(',
        r'exec\(',
        r'__import__\(',
        r'compile\(',
        r'os\.popen\(',
    ]
    
    @staticmethod
    def contains_system_file_deletion(code: str) -> Tuple[bool, List[str]]:
        """Check if code attempts to delete or modify system files"""
        dangerous_operations = []
        
        for pattern in SystemFileProtector.PROTECTED_SYSTEM_PATHS:
            if re.search(pattern, code, re.IGNORECASE):
                dangerous_operations.append(f"Blocked: Attempt to access/modify system path (pattern: {pattern})")
        
        # Check for high-risk operations that could be used to delete system files
        lines = code.split('\n')
        for i, line in enumerate(lines, 1):
            # Look for file deletion operations without specific paths (could be variable-based)
            if any(op in line.lower() for op in ['os.remove', 'shutil.rmtree', 'os.unlink']):
                # Check if it's using a variable (hard to determine path)
                if any(var in line for var in ['path', 'file', 'dir']):
                    dangerous_operations.append(f"Line {i}: File deletion operation with variable - requires manual review")
        
        return len(dangerous_operations) > 0, dangerous_operations
    
    @staticmethod
    def contains_high_risk_commands(code: str) -> Tuple[bool, List[str]]:
        """Check for high-risk commands that could be dangerous"""
        warnings = []
        
        for pattern in SystemFileProtector.HIGH_RISK_COMMANDS:
            if re.search(pattern, code):
                warnings.append(f"Warning: High-risk command detected (pattern: {pattern})")
        
        return len(warnings) > 0, warnings

class ModuleAutoInstaller:
    """Automatically installs missing Python modules"""
    
    @staticmethod
    def extract_imports(code: str) -> List[str]:
        """Extract all imported modules from code"""
        imports = set()
        
        # Simple regex-based extraction (faster than AST for this use case)
        import_patterns = [
            r'^\s*import\s+([\w\.]+)',
            r'^\s*from\s+([\w\.]+)\s+import',
            r'^\s*import\s+([\w\.]+)\s+as',
            r'^\s*from\s+([\w\.]+)\s+import\s+',
        ]
        
        for line in code.split('\n'):
            for pattern in import_patterns:
                match = re.match(pattern, line)
                if match:
                    module_name = match.group(1).split('.')[0]
                    imports.add(module_name)
        
        # Remove built-in modules
        builtin_modules = {
            'os', 'sys', 'math', 'datetime', 'json', 're', 'random', 
            'collections', 'itertools', 'functools', 'typing', 'pathlib',
            'subprocess', 'shutil', 'tempfile', 'warnings', 'importlib',
            'builtins', 'io', 'csv', 'html', 'http', 'ssl', 'socket',
            'email', 'urllib', 'xml', 'sqlite3', 'hashlib', 'base64',
            'logging', 'threading', 'multiprocessing', 'asyncio',
            'decimal', 'fractions', 'statistics', 'copy', 'pprint',
            'textwrap', 'string', 'difflib', 'time', 'calendar'
        }
        
        return [imp for imp in imports if imp not in builtin_modules]
    
    @staticmethod
    def install_module(module_name: str) -> bool:
        """Install a module using pip"""
        try:
            # Check if already installed
            try:
                importlib.import_module(module_name)
                return True
            except ImportError:
                pass
            
            # Install the module
            print(f"📦 Installing missing module: {module_name}")
            result = subprocess.run(
                [sys.executable, "-m", "pip", "install", module_name],
                capture_output=True,
                text=True,
                timeout=60
            )
            
            if result.returncode == 0:
                print(f"✅ Successfully installed {module_name}")
                return True
            else:
                print(f"❌ Failed to install {module_name}: {result.stderr}")
                return False
                
        except subprocess.TimeoutExpired:
            print(f"⏰ Timeout installing {module_name}")
            return False
        except Exception as e:
            print(f"⚠️ Error installing {module_name}: {e}")
            return False
    
    @staticmethod
    def ensure_all_modules(code: str) -> bool:
        """Ensure all required modules are installed"""
        imports = ModuleAutoInstaller.extract_imports(code)
        
        if not imports:
            return True
        
        print(f"🔍 Found imports: {', '.join(imports)}")
        
        for module in imports:
            if not ModuleAutoInstaller.install_module(module):
                return False
        
        return True

class CodeGenerator:
    """Generates code using Groq with strict instructions"""
    
    @staticmethod
    def generate_python_code(user_request: str, max_retries: int = 2) -> Optional[str]:
        """Generate Python code from user request with strict formatting"""
        
        system_prompt = """You are an expert Python code generator. Generate ONLY Python code with these strict rules:

1. OUTPUT ONLY RAW PYTHON CODE - NO MARKDOWN, NO EXPLANATIONS, NO COMMENTS (except docstrings if absolutely necessary)
2. Code must be error-free and ready to execute immediately
3. Include all necessary imports at the top
4. If the request is ambiguous, implement the most common/useful interpretation
5. Add error handling (try-except) for operations that might fail
6. The code should be complete and executable
7. NEVER include examples, explanations, or any text outside the code
8. If writing to files, use safe paths (avoid system directories)
9. Make the code robust and production-ready

Format example (don't include this text in output):
import os
import webbrowser

def main():
    try:
        webbrowser.open('https://google.com')
        print("Successfully opened Google")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()

Remember: ONLY the Python code, nothing else!"""
        
        for attempt in range(max_retries):
            try:
                response = client.chat.completions.create(
                    messages=[
                        {"role": "system", "content": system_prompt},
                        {"role": "user", "content": f"Generate Python code for: {user_request}"}
                    ],
                    model="llama-3.3-70b-versatile",
                    temperature=0.1,
                    max_tokens=2000
                )
                
                code = response.choices[0].message.content.strip()
                
                # Clean any markdown code blocks
                if code.startswith("```python"):
                    code = code[9:]
                elif code.startswith("```"):
                    code = code[3:]
                if code.endswith("```"):
                    code = code[:-3]
                code = code.strip()
                
                # Validate it's Python code
                if "import " in code or "def " in code or "print(" in code:
                    print(f"✅ Code generated successfully (attempt {attempt + 1})")
                    return code
                else:
                    print(f"⚠️  Generated code doesn't look like Python, retrying...")
                    
            except Exception as e:
                print(f"❌ Attempt {attempt + 1} failed: {e}")
                if attempt == max_retries - 1:
                    return None
        
        return None

class CodeExecutor:
    """Executes generated Python code safely"""
    
    @staticmethod
    def execute_code(code: str, timeout: int = 30) -> Dict:
        """Execute Python code with safety checks"""
        
        result = {
            "success": False,
            "output": "",
            "error": None,
            "execution_time": 0
        }
        
        import time
        start_time = time.time()
        
        # Create temporary Python file
        with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False) as f:
            f.write(code)
            temp_file = f.name
        
        try:
            # Execute the code
            process = subprocess.run(
                [sys.executable, temp_file],
                capture_output=True,
                text=True,
                timeout=timeout,
                env=os.environ.copy()
            )
            
            result["output"] = process.stdout
            result["success"] = process.returncode == 0
            
            if process.stderr:
                result["error"] = process.stderr
            
        except subprocess.TimeoutExpired:
            result["error"] = f"Execution timed out after {timeout} seconds"
        except Exception as e:
            result["error"] = f"Execution error: {str(e)}"
        finally:
            # Clean up
            try:
                os.unlink(temp_file)
            except:
                pass
            
            result["execution_time"] = time.time() - start_time
        
        return result

def ai_code_executor(user_request: str, auto_execute: bool = True) -> Dict:
    """
    POWERFUL function that generates and executes Python code based on ANY request
    
    Args:
        user_request (str): What you want the code to do
        auto_execute (bool): Whether to execute the generated code
    
    Returns:
        Dict with results, code, and execution info
    """
    
    print(f"\n{'='*60}")
    print(f"🤖 PROCESSING REQUEST: {user_request}")
    print(f"{'='*60}\n")
    
    result = {
        "request": user_request,
        "code_generated": False,
        "code": None,
        "execution_success": False,
        "output": None,
        "error": None,
        "warnings": [],
        "modules_installed": []
    }
    
    # Step 1: Generate code
    print("🔧 Generating Python code...")
    code = CodeGenerator.generate_python_code(user_request)
    
    if not code:
        result["error"] = "Failed to generate code"
        return result
    
    result["code"] = code
    result["code_generated"] = True
    
    # Step 2: Safety check - ONLY for system file deletion
    print("🔒 Running safety check (system file protection only)...")
    has_dangerous_ops, dangerous_details = SystemFileProtector.contains_system_file_deletion(code)
    has_high_risk, risk_warnings = SystemFileProtector.contains_high_risk_commands(code)
    
    result["warnings"].extend(risk_warnings)
    
    if has_dangerous_ops:
        print(f"❌❌❌ BLOCKED: Code contains dangerous system file operations! ❌❌❌")
        for detail in dangerous_details:
            print(f"   ⚠️  {detail}")
        
        # Show snippet of problematic code
        print("\n🚫 Problematic code snippet:")
        lines = code.split('\n')
        for i, line in enumerate(lines, 1):
            if any(pattern in line.lower() for pattern in ['system32', 'rm -rf', 'format', 'chkdsk']):
                print(f"   Line {i}: {line[:100]}...")
        
        result["error"] = "Code blocked - contains dangerous system file operations"
        return result
    
    # Step 3: Install required modules
    print("📦 Checking/installing required modules...")
    if not ModuleAutoInstaller.ensure_all_modules(code):
        result["error"] = "Failed to install required modules"
        return result
    
    # Step 4: Execute code if requested
    if auto_execute:
        print("⚡ Executing generated code...")
        execution_result = CodeExecutor.execute_code(code, timeout=60)
        
        result["execution_success"] = execution_result["success"]
        result["output"] = execution_result["output"]
        result["execution_time"] = execution_result["execution_time"]
        
        if execution_result["error"]:
            result["error"] = execution_result["error"]
        
        if execution_result["success"]:
            print(f"✅ Execution completed in {execution_result['execution_time']:.2f}s")
        else:
            print(f"❌ Execution failed")
    else:
        print("⏸️  Code generation complete - execution skipped")
    
    return result

def execute_anything(request: str) -> None:
    """
    The ultimate function - takes ANY request, generates code, and executes it
    Only blocks if it detects system file deletion attempts
    """
    print(f"\n{'🚀'*20}")
    print(f"EXECUTE ANYTHING MODE ACTIVATED")
    print(f"{'🚀'*20}\n")
    
    result = ai_code_executor(request, auto_execute=True)
    
    print(f"\n{'='*60}")
    print(f"RESULTS:")
    print(f"{'='*60}")
    
    if result["code_generated"]:
        print(f"✅ Code generated successfully")
        
        if result["execution_success"]:
            print(f"✅ Code executed successfully")
            
            if result["output"]:
                print(f"\n📤 Output:")
                print(f"{'-'*40}")
                print(result["output"])
                print(f"{'-'*40}")
        else:
            print(f"❌ Execution failed")
            
    if result["error"]:
        print(f"❌ Error: {result['error']}")
    
    if result["warnings"]:
        print(f"\nWarnings:")
        for warning in result["warnings"]:
            print(f"   • {warning}")
    
    print(f"{'='*60}\n")

