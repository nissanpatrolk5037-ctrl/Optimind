import json
import os

# ------------------ MEMORY FILE ------------------
MEMORY_FILE = "E:\\Optimind\\memory\\conversation_memory.json"

def log_conversation(user_text: str, assistant_text: str):
    """Append conversation to memory file."""
    memory = []
    if os.path.exists(MEMORY_FILE):
        try:
            with open(MEMORY_FILE, "r", encoding="utf-8") as f:
                memory = json.load(f)
        except Exception:
            memory = []

    memory.append({
        "user": user_text,
        "assistant": assistant_text
    })

    try:
        with open(MEMORY_FILE, "w", encoding="utf-8") as f:
            json.dump(memory, f, indent=4, ensure_ascii=False)
    except Exception as e:
        print(f"[Memory Error] {e}")
