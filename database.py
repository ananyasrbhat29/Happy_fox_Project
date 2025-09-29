import sqlite3

DB_NAME = "emails.db"

def init_db():
    
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS emails (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            gmail_id TEXT UNIQUE,
            sender TEXT,
            subject TEXT,
            snippet TEXT
        )
    """)
    conn.commit()
    conn.close()
    print("✅ Database initialized.")

def save_email(sender, subject, snippet, gmail_id):
    """Save an email to the database."""
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    try:
        c.execute(
            "INSERT INTO emails (gmail_id, sender, subject, snippet) VALUES (?, ?, ?, ?)",
            (gmail_id, sender, subject, snippet)
        )
        conn.commit()
        print(f"Saved email: {subject}")
    except sqlite3.IntegrityError:
        print(f"Email already exists: {subject}")
    conn.close()

def get_all_emails():
    
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("SELECT gmail_id, sender, subject, snippet FROM emails")
    emails = c.fetchall()
    conn.close()
    return emails
