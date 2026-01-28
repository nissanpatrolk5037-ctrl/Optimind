import os
import sqlite3
import hashlib
import ctypes
import sys
import datetime
import time

# ===================== CONFIG =====================

DB_FILE = "E:\\Optimind\\security-db\\age_guard.db"
MIN_AGE = 18

HOSTS_PATH = r"C:\Windows\System32\drivers\etc\hosts"
REDIRECT_IP = "127.0.0.1"

BLOCKED_SITES_UNDERAGE = [
    # Porn
    "pornhub.com",
    "www.pornhub.com",
    "xvideos.com",
    "www.xvideos.com",
    "xnxx.com",
    "www.xnxx.com",
    "redtube.com",
    "www.redtube.com",
    "youporn.com",
    "www.youporn.com",

    # Piracy
    "thepiratebay.org",
    "www.thepiratebay.org",
    "1337x.to",
    "www.1337x.to",
    "rarbg.to",
    "www.rarbg.to",

    # Illegal / grey
    "dark.fail",
    "www.dark.fail",
    "pastebin.com",
    "www.pastebin.com"
]

# ===================== ADMIN CHECK =====================

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

# ===================== HASHING =====================

def sha256(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()

# ===================== DATABASE =====================

def init_db():
    conn = sqlite3.connect(DB_FILE)
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS age_data (
            id INTEGER PRIMARY KEY CHECK (id = 1),
            age_hash TEXT NOT NULL,
            created_at TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()

def age_exists() -> bool:
    conn = sqlite3.connect(DB_FILE)
    cur = conn.cursor()
    cur.execute("SELECT age_hash FROM age_data WHERE id = 1")
    row = cur.fetchone()
    conn.close()
    return row is not None

def store_age(age: int):
    conn = sqlite3.connect(DB_FILE)
    cur = conn.cursor()

    age_hash = sha256(str(age))
    now = datetime.datetime.utcnow().isoformat()

    cur.execute("DELETE FROM age_data")
    cur.execute(
        "INSERT INTO age_data (id, age_hash, created_at) VALUES (1, ?, ?)",
        (age_hash, now)
    )

    conn.commit()
    conn.close()

def verify_age(target_age: int) -> bool:
    conn = sqlite3.connect(DB_FILE)
    cur = conn.cursor()

    cur.execute("SELECT age_hash FROM age_data WHERE id = 1")
    row = cur.fetchone()
    conn.close()

    if not row:
        return False

    expected = sha256(str(target_age))
    return row[0] == expected

# ===================== HOSTS FILE CONTROL =====================

def block_sites():
    with open(HOSTS_PATH, "r+") as file:
        content = file.read()
        for site in BLOCKED_SITES_UNDERAGE:
            entry = f"{REDIRECT_IP} {site}"
            if entry not in content:
                file.write(entry + "\n")

def unblock_sites():
    with open(HOSTS_PATH, "r+") as file:
        lines = file.readlines()
        file.seek(0)
        for line in lines:
            if not any(site in line for site in BLOCKED_SITES_UNDERAGE):
                file.write(line)
        file.truncate()

# ===================== MAIN LOGIC =====================

def run_age_guard():
    if not is_admin():
        ctypes.windll.shell32.ShellExecuteW(
            None, "runas", sys.executable,
            " ".join(sys.argv), None, 1
        )
        sys.exit(0)

    init_db()

    if not age_exists():
        try:
            age = int(input("Enter your age: ").strip())
            store_age(age)
        except:
            print("[AGE GUARD] Invalid input")
            return

    # brute-safe verification (no reverse possible)
    underage = True
    for a in range(1, MIN_AGE):
        if verify_age(a):
            underage = True
            break
    else:
        underage = False

    if underage:
        block_sites()
        print("[AGE GUARD] Underage detected — restricted sites BLOCKED")
    else:
        unblock_sites()
        print("[AGE GUARD] Age verified — no restrictions")


