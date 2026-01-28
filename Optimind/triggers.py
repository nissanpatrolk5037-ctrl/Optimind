aws_triggers = [
    # Basic commands
    "aws control", "control aws", "manage aws", "handle aws",
    "ec2 control", "control ec2", "manage ec2", "handle ec2",
    
    # Start/Stop instances
    "start instance", "stop instance", "start ec2", "stop ec2",
    "start aws instance", "stop aws instance", "start server", "stop server",
    "launch instance", "terminate instance", "boot instance", "shutdown instance",
    
    # AWS specific
    "amazon web services", "aws management", "cloud control",
    "control cloud instance", "manage cloud server",
    
    # Casual
    "handle the aws", "manage the ec2", "control the server",
    "turn on aws", "turn off aws", "start the cloud", "stop the cloud",
]

google_drive_triggers = [
    # Basic upload
    "upload to google drive", "upload to drive", "backup to google drive",
    "save to google drive", "store in google drive", "put in google drive",
    
    # File operations
    "upload file to drive", "upload document to drive", "upload image to drive",
    "upload video to drive", "upload folder to drive",
    
    # Backup operations
    "backup to drive", "save backup to drive", "cloud backup", "google backup",
    "drive backup", "backup files to drive",
    
    # Cloud storage
    "cloud storage upload", "google cloud upload", "drive storage",
    "store in the cloud", "save to cloud",
    
    # Casual
    "put it on drive", "save it to drive", "backup to google",
    "upload to my drive", "save to my drive",
]

calendar_triggers = [
    # Schedule events
    "schedule event", "create calendar event", "add to calendar",
    "schedule meeting", "set up event", "plan event",
    
    # Calendar operations
    "add calendar event", "create event", "make an appointment",
    "set reminder", "create reminder", "schedule appointment",
    
    # Google Calendar
    "google calendar", "gcalendar event", "google meet schedule",
    "calendar schedule", "add to google calendar",
    
    # Time management
    "plan meeting", "set up meeting", "arrange meeting",
    "book time", "reserve time", "set event",
    
    # Casual
    "put it on my calendar", "add to my calendar", "schedule it",
    "set a time", "make a plan",
]

discord_triggers = [
    # Send messages
    "send discord message", "discord message", "post on discord",
    "send to discord", "message on discord", "chat on discord",
    
    # Channel operations
    "send to discord channel", "post in discord", "discord post",
    "send discord chat", "send discord notification",
    
    # Bot commands
    "discord bot send", "send via discord", "discord send",
    "message discord channel", "post to discord server",
    
    # Casual
    "tell discord", "send to the discord", "post on the discord",
    "message the discord", "chat on the discord",
]

whatsapp_triggers = [
    # Send messages
    "send whatsapp message", "whatsapp message", "send on whatsapp",
    "message on whatsapp", "chat on whatsapp", "whatsapp chat",
    
    # App specific
    "send whatsapp", "whatsapp send", "message via whatsapp",
    "whatsapp notification", "whatsapp alert",
    
    # Casual
    "text on whatsapp", "whatsapp text", "send a whatsapp",
    "message on whatsapp", "whatsapp me",
]

email_triggers = [
    # Single email
    "send email", "email message", "send an email",
    "mail message", "send mail", "email someone",
    
    # Email operations
    "compose email", "write email", "draft email",
    "send message via email", "email communication",
    
    # Casual
    "send an email", "email it", "mail it",
    "send via email", "email to",
]

bulk_email_triggers = [
    # Multiple emails
    "send multiple emails", "send bulk emails", "email blast",
    "mass email", "send to many emails", "email campaign",
    
    # Bulk operations
    "send to all", "email everyone", "notify all via email",
    "send group email", "email distribution",
    
    # Casual
    "email blast", "mass mail", "send to many",
    "email all", "notify everyone",
]

attachment_triggers = [
    # Download attachments
    "download email attachments", "download attachments", "save email attachments",
    "get email files", "extract email attachments", "save attachments from email",
    
    # File operations
    "download files from email", "save email files", "get attachments",
    "extract files from email", "backup email attachments",
    
    # Casual
    "get the attachments", "save the email files", "download the files",
    "backup attachments", "save attachments",
]


screen_triggers = [
    "look at my screen", "describe my screen", 
    "summarize my screen", "see my screen",
    "what's on my screen", "read my screen"
]

image_triggers = [
    # Basic image creation
    "generate an image", "make an image", "create an image", "build an image",
    "draw an image", "produce an image", "design an image", "render an image",
    "craft an image", "sketch an image", "paint an image", "illustrate an image",
    
    # Picture synonyms
    "generate a picture", "make a picture", "create a picture", "build a picture",
    "draw a picture", "paint a picture", "sketch a picture", "illustrate a picture",
    
    # Photo synonyms
    "generate a photo", "make a photo", "create a photo", "build a photo",
    "take a photo", "capture a photo", "produce a photo",
    
    # Visual content
    "generate visual content", "make visual content", "create visual content",
    "build visual content", "produce visual content", "design visual content",
    
    # Artwork
    "generate artwork", "make artwork", "create artwork", "build artwork",
    "produce artwork", "design artwork", "craft artwork",
    
    # Graphics
    "generate a graphic", "make a graphic", "create a graphic", "build a graphic",
    "design a graphic", "produce a graphic", "craft a graphic",
    
    # Specific image types
    "generate a banner", "make a banner", "create a banner", "design a banner",
    "generate a poster", "make a poster", "create a poster", "design a poster",
    "generate a logo", "make a logo", "create a logo", "design a logo",
    "generate an icon", "make an icon", "create an icon", "design an icon",
    "generate an avatar", "make an avatar", "create an avatar", "design an avatar",
    "generate a thumbnail", "make a thumbnail", "create a thumbnail",
    
    # More casual
    "whip up an image", "throw together an image", "put together an image",
    "come up with an image", "develop an image",
]

qr_code_triggers = [
    # Standard formats
    "generate a qrcode", "make a qrcode", "create a qrcode", "build a qrcode",
    "produce a qrcode", "design a qrcode", "craft a qrcode",
    
    # With space
    "generate a qr code", "make a qr code", "create a qr code", "build a qr code",
    "produce a qr code", "design a qr code", "craft a qr code",
    
    # Full name
    "generate a quick response code", "make a quick response code",
    "create a quick response code", "build a quick response code",
    
    # Abbreviated
    "generate qr", "make qr", "create qr", "build qr",
    "produce qr", "design qr", "craft qr",
    
    # Related
    "create a barcode", "generate a barcode", "make a barcode",
    "build a barcode", "produce a barcode", "design a barcode",
    
    # Actions
    "scan a qrcode", "read a qrcode", "decode a qrcode",
    "make a scannable code", "create a scannable code",
    
    # Casual
    "whip up a qr code", "throw together a qr code",
    "put together a qr code", "come up with a qr code",
]

wordcloud_triggers = [
    # One word
    "generate a wordcloud", "make a wordcloud", "create a wordcloud", "build a wordcloud",
    "produce a wordcloud", "design a wordcloud", "craft a wordcloud",
    
    # Two words
    "generate a word cloud", "make a word cloud", "create a word cloud", "build a word cloud",
    "produce a word cloud", "design a word cloud", "craft a word cloud",
    
    # Word art
    "generate word art", "make word art", "create word art", "build word art",
    "produce word art", "design word art", "craft word art",
    
    # Tag cloud
    "generate a tag cloud", "make a tag cloud", "create a tag cloud", "build a tag cloud",
    "produce a tag cloud", "design a tag cloud", "craft a tag cloud",
    
    # Text visualization
    "visualize text", "create text visualization", "generate text visualization",
    "make text visualization", "build text visualization",
    
    # Word frequency
    "show word frequency", "visualize word frequency", "create word frequency chart",
    "generate word frequency visualization",
    
    # Casual
    "whip up a word cloud", "throw together a word cloud",
    "put together a word cloud", "come up with a word cloud",
]

report_triggers = [
    # Standard report
    "generate a report", "make a report", "create a report", "build a report", "write a report",
    "compile a report", "prepare a report", "produce a report", "develop a report",
    "draft a report", "formulate a report", "assemble a report",
    
    # Summary
    "generate a summary", "make a summary", "create a summary", "build a summary",
    "write a summary", "compile a summary", "prepare a summary", "produce a summary",
    
    # Document
    "generate a document", "make a document", "create a document", "build a document",
    "write a document", "compile a document", "prepare a document", "produce a document",
    
    # Analysis
    "generate an analysis", "make an analysis", "create an analysis", "build an analysis",
    "write an analysis", "compile an analysis", "prepare an analysis", "produce an analysis",
    
    # Review
    "generate a review", "make a review", "create a review", "build a review",
    "write a review", "compile a review", "prepare a review", "produce a review",
    
    # Evaluation
    "generate an evaluation", "make an evaluation", "create an evaluation",
    "write an evaluation", "compile an evaluation",
    
    # Assessment
    "generate an assessment", "make an assessment", "create an assessment",
    "write an assessment", "compile an assessment",
    
    # Specific types
    "generate a progress report", "create a progress report", "write a progress report",
    "generate a status report", "create a status report", "write a status report",
    "generate a financial report", "create a financial report", "write a financial report",
    "generate a sales report", "create a sales report", "write a sales report",
    
    # Casual
    "whip up a report", "throw together a report", "put together a report",
    "come up with a report", "knock out a report",
]

audio_triggers = [
    # Audio content
    "generate an audio", "make an audio", "create an audio", "build an audio",
    "produce an audio", "design an audio", "craft an audio",
    
    # Sound
    "generate sound", "make sound", "create sound", "build sound",
    "produce sound", "design sound", "craft sound",
    
    # Audio file
    "generate an audio file", "make an audio file", "create an audio file",
    "build an audio file", "produce an audio file",
    
    # Synthesis
    "synthesize audio", "synthesize sound", "generate synthetic audio",
    "create synthetic sound", "produce synthesized audio",
    
    # Casual
    "whip up some audio", "throw together some audio", "put together some audio",
    "come up with audio", "make some sound",
]

# Git Triggers
git_triggers = [
    # Basic operations
    "git status", "check git status", "repository status",
    "git commit", "commit changes", "save changes",
    "git push", "push to github", "upload changes",
    "git pull", "pull updates", "get latest changes",
    "git clone", "clone repository", "download repo",
    
    # Branch operations
    "git branch", "list branches", "show branches",
    "create branch", "new branch", "make branch",
    "switch branch", "change branch", "checkout branch",
    "delete branch", "remove branch",
    
    # History and logs
    "git log", "show commits", "commit history",
    "view history", "see changes", "git history",
    
    # General Git
    "version control", "git operations", "repository",
    "git add", "stage changes", "track files",
    "git merge", "merge branches", "combine changes",
    "git stash", "save changes temporarily", "stash changes",
    
    # Remote operations
    "remote", "origin", "upstream", "git remote",
    "fetch", "git fetch", "get remote changes",
    
    # Specific commands
    "git init", "initialize repository", "create repo",
    "git diff", "see differences", "what changed",
    "git reset", "undo changes", "revert commit",
    "git revert", "revert changes", "undo commit",
    "git tag", "create tag", "version tag",
    
    # Services
    "github", "gitlab", "bitbucket", "git hub",
    
    # Common phrases
    "what's in my repo", "my repository", "source control",
    "code changes", "project changes", "track changes",
    "sync repository", "sync with remote", "update repository"
]

slack_triggers = [
    "slack", "send slack", "post to slack", "slack message", "message slack"
]

twitter_triggers = [
    "tweet", "post tweet", "twitter", "x post", "post to twitter"
]

telegram_triggers = [
    "telegram", "send telegram", "telegram message", "tg message"
]

# Cloud & Infrastructure
github_triggers = [
    "github", "create repo", "new repository", "github repository"
]

azure_triggers = [
    "azure", "azure vm", "vm control", "virtual machine", "azure virtual machine"
]

dropbox_triggers = [
    "dropbox", "upload to dropbox", "dropbox upload", "save to dropbox"
]

docker_triggers = [
    "docker", "container", "docker container", "docker control", "start container", "stop container"
]

# AI & Processing
openai_triggers = [
    "openai", "chat gpt", "gpt", "chatgpt", "ai chat", "ask ai"
]

translate_triggers = [
    # Basic translation
    "translate", "translation", "translate text", "convert language",
    "language translation", "text translation", "interpret",
    
    # Specific languages
    "to english", "to spanish", "to french", "to german", "to chinese",
    "to japanese", "to hindi", "to arabic", "to russian", "to portuguese",
    "to italian", "to korean", "to dutch", "to greek", "to turkish",
    
    # Reverse translation
    "from english", "from spanish", "from french", "from german",
    "from chinese", "from japanese", "from hindi", "from arabic",
    
    # Actions
    "convert to", "change language", "make it", "say it in",
    "what is this in", "how do you say", "translate this",
    
    # Language detection
    "what language", "detect language", "identify language",
    "language of", "which language", "language detection",
    
    # Common phrases
    "english translation", "spanish version", "french equivalent",
    "german meaning", "chinese characters", "japanese text",
    
    # Specific use cases
    "translate document", "translate website", "translate email",
    "translate message", "translate chat", "translate paragraph",
    "translate sentence", "translate word", "translate phrase",
    
    # Multilingual
    "multilingual", "bilingual", "different language", "foreign language",
    "international", "cross-language", "language conversion"
]

wikipedia_triggers = [
    "wikipedia", "wiki", "search wiki", "look up", "encyclopedia"
]

# Media & Files
youtube_triggers = [
    "youtube", "download video", "youtube download", "save youtube", "yt download"
]

pdf_triggers = [
    # Basic PDF creation
    "pdf", "create pdf", "generate pdf", "make pdf", "pdf document",
    "pdf file", "export to pdf", "save as pdf", "print to pdf",
    
    # Content types
    "text to pdf", "document to pdf", "convert to pdf", "export pdf",
    "html to pdf", "webpage to pdf", "html document to pdf",
    "image to pdf", "picture to pdf", "photo to pdf", "scan to pdf",
    
    # Specific use cases
    "create document", "generate report", "make certificate",
    "create invoice", "generate receipt", "create form",
    "make brochure", "create manual", "generate guide",
    
    # Actions with PDF
    "save as pdf", "download pdf", "export as pdf", "convert file to pdf",
    "make a pdf from", "create pdf from text", "pdf version",
    
    # Common phrases
    "pdf format", "portable document format", "adobe pdf",
    "pdf creator", "pdf generator", "pdf maker",
    
    # Document types
    "report pdf", "letter pdf", "memo pdf", "contract pdf",
    "agreement pdf", "proposal pdf", "presentation pdf",
    
    # Features
    "add to pdf", "merge pdf", "split pdf", "edit pdf",
    "pdf pages", "multiple pages pdf", "pdf with images",
    
    # Automation
    "automate pdf", "batch pdf", "generate multiple pdfs",
    "pdf template", "pdf automation", "pdf script"
]

screenshot_triggers = [
    "screenshot", "screen capture", "capture screen", "take screenshot"
]

ocr_triggers = [
    "ocr", "extract text", "read text", "text recognition", "scan text", "image to text"
]

video_convert_triggers = [
    "convert video", "video conversion", "change format", "video format", "mp4 convert"
]

audio_extract_triggers = [
    "extract audio", "audio from video", "get audio", "save audio", "mp3 from video"
]

# Data & Analysis
excel_triggers = [
    "excel", "spreadsheet", "xlsx", "read excel", "write excel", "excel file"
]

database_triggers = [
    "database", "sql", "query database", "mysql", "postgres", "sqlite"
]

data_viz_triggers = [
    "chart", "graph", "visualize", "data visualization", "plot", "visualization"
]

weather_triggers = [
    "weather", "temperature", "forecast", "humidity", "weather info"
]

stock_triggers = [
    "stock", "share price", "market", "ticker", "stock market", "stock price"
]

currency_triggers = [
    "currency", "convert money", "exchange rate", "currency conversion", "forex"
]

# Security & Utilities
encrypt_triggers = [
    "encrypt", "decrypt", "encryption", "decryption", "secure file", "crypt"
]

password_triggers = [
    "password", "generate password", "random password", "secure password", "password generator"
]

url_shorten_triggers = [
    "shorten", "url shortener", "bitly", "short link", "tinyurl"
]

domain_lookup_triggers = [
    # Basic domain lookup
    "domain", "domain lookup", "whois", "domain information",
    "check domain", "domain check", "lookup domain", "domain search",
    
    # Specific information types
    "whois lookup", "domain whois", "registration info", "domain registration",
    "domain owner", "domain registrar", "domain expiration", "when does domain expire",
    
    # DNS information
    "dns records", "domain dns", "name servers", "dns lookup",
    "mx records", "a records", "txt records", "domain servers",
    
    # SSL/security
    "ssl certificate", "domain ssl", "https certificate", "security certificate",
    "domain security", "ssl check", "certificate info",
    
    # Network information
    "domain ip", "ip address", "server ip", "hosting info",
    "where is domain hosted", "domain location", "ip lookup",
    
    # Website information
    "website info", "site information", "web domain", "url information",
    "check website", "website lookup", "site check",
    
    # Expiration and age
    "domain age", "how old is domain", "when created", "registration date",
    "expiration date", "when expires", "domain expiry",
    
    # Availability
    "is domain available", "domain available", "check availability",
    "register domain", "buy domain", "domain for sale",
    
    # Popular domains
    "google.com info", "check facebook domain", "amazon domain info",
    "twitter domain", "github domain", "instagram domain",
    
    # Technical details
    "nameservers", "dns settings", "domain configuration",
    "domain settings", "domain setup", "domain technical info",
    
    # Ownership
    "who owns", "domain ownership", "owner information",
    "registrant info", "contact info", "domain contacts",
    
    # Status
    "domain status", "is domain active", "domain working",
    "domain reachable", "ping domain", "domain response"
]

hash_triggers = [
    "hash", "generate hash", "md5", "sha256", "checksum", "hash generator"
]

# System & Network
system_info_triggers = [
    "system info", "system information", "cpu", "memory", "disk", "system stats"
]

process_control_triggers = [
    "process", "kill process", "start process", "stop process", "process list", "running processes"
]

backup_triggers = [
    "backup", "backup files", "copy files", "archive", "zip files"
]

network_scan_triggers = [
    "network scan", "port scan", "nmap", "scan network", "network devices"
]

ssh_triggers = [
    "ssh", "remote", "execute command", "remote server", "ssh connect"
]

# Automation
web_scrape_triggers = [
    "scrape", "web scrape", "extract data", "scrape website", "crawl"
]

file_ops_triggers = [
    "copy file", "move file", "delete file", "rename file", "file operation", "organize files"
]

git_triggers = [
    "git", "clone", "pull", "push", "commit", "repository", "version control"
]

api_test_triggers = [
    # Basic API testing
    "api test", "test api", "api request", "http request", "rest api",
    "api call", "test endpoint", "api check", "api validation",
    
    # HTTP methods
    "get request", "post request", "put request", "delete request",
    "patch request", "http get", "http post", "http put", "http delete",
    
    # API endpoints
    "test endpoint", "check api", "api health", "api status",
    "ping api", "api connectivity", "api response",
    
    # Specific testing
    "json api", "restful api", "web api", "api endpoint",
    "api url", "service endpoint", "microservice test",
    
    # Load testing
    "load test", "stress test", "performance test", "api performance",
    "concurrent users", "api load", "stress api", "benchmark api",
    
    # Monitoring
    "api monitor", "api health check", "service health", "uptime check",
    "api availability", "service status", "api dashboard",
    
    # Debugging
    "debug api", "api debug", "troubleshoot api", "api error",
    "api problem", "fix api", "api issue",
    
    # Documentation
    "api documentation", "swagger test", "openapi test", "api spec",
    "test swagger", "openapi endpoint", "api schema",
    
    # Authentication
    "api auth", "test authentication", "oauth test", "jwt test",
    "api key test", "bearer token", "auth endpoint",
    
    # Specific APIs
    "test webhook", "webhook endpoint", "callback url", "notification api",
    "payment api", "stripe test", "paypal api", "github api", "twitter api",
    
    # Tools
    "postman", "insomnia", "curl test", "http client", "api client",
    "rest client", "api tool", "http tool"
]

load_test_triggers = [
    "load test", "stress test", "performance test", "api load",
    "concurrent users", "stress api", "benchmark api", "api performance",
    "multiple requests", "parallel requests", "high traffic",
    "break api", "test limits", "api capacity", "scalability test",
    "volume test", "endurance test", "soak test", "spike test"
]

log_analyze_triggers = [
    # Basic log analysis
    "log", "analyze log", "log analysis", "parse log", "log file",
    "check logs", "log parser", "log review", "system logs",
    
    # Specific log types
    "error log", "access log", "server log", "application log",
    "nginx log", "apache log", "web server log", "database log",
    
    # Analysis types
    "find errors", "count errors", "log statistics", "log metrics",
    "log patterns", "log trends", "log summary", "log report",
    
    # Error analysis
    "show errors", "error analysis", "debug errors", "troubleshoot logs",
    "error messages", "exception log", "crash log", "failure analysis",
    
    # Performance analysis
    "performance logs", "response time", "slow logs", "latency analysis",
    "throughput logs", "performance metrics", "bottleneck analysis",
    
    # Security analysis
    "security logs", "audit log", "intrusion detection", "suspicious activity",
    "failed login", "access violation", "security audit", "threat detection",
    
    # Monitoring
    "log monitoring", "real-time logs", "log watch", "log tail",
    "live logs", "log stream", "monitor logs", "log dashboard",
    
    # Search and filter
    "search logs", "filter logs", "grep logs", "find in logs",
    "log search", "text search", "pattern search", "regex search",
    
    # Specific patterns
    "find ip addresses", "extract urls", "user activity", "session tracking",
    "api calls", "http requests", "status codes", "response codes",
    
    # Time-based
    "hourly logs", "daily logs", "time range", "log timeline",
    "peak hours", "busiest time", "traffic patterns", "time analysis",
    
    # File operations
    "read log", "open log", "process log", "export log",
    "log export", "save analysis", "generate report", "log summary",
    
    # Common tools
    "logstash", "elk", "splunk", "graylog", "fluentd",
    "log analyzer", "log insight", "log intelligence"
]

live_camera_triggers = [
    "live camera", "camera detection", "webcam detection",
    "live detection", "real-time detection", "start camera",
    "open camera", "camera stream", "live stream", "webcam stream",
    "camera feed", "live feed", "start webcam", "turn on camera",
    "camera view", "live view", "real-time camera", "video detection",
    "video stream", "detect live", "recognize live", "live object detection",
    "real-time object detection", "camera object detection"
]

image_object_detection_triggers = [
    "object detection", "detect objects", "recognize the objects",
    "recognize objects", "detect object", "recognize the object",
    "recognize object", "object recognition", "detect these objects",
    "recognize these objects", "find objects", "identify objects",
    "what objects are in this", "what is in this image",
    "detect everything", "recognize everything", "show me the objects",
    "label the objects", "find all objects", "scan for objects",
    "object scan", "image analysis", "analyze image", "detect items",
    "recognize items", "detect things", "recognize things"
]


