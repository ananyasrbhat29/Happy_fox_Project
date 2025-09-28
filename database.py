import sqlite3
import csv
import os

def init_db():
    conn = sqlite3.connect('emails.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS emails (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            sender TEXT,
            subject TEXT,
            snippet TEXT
        )
    ''')
    conn.commit()
    conn.close()

    if not os.path.exists('emails.csv'):
        with open('emails.csv', 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['Sender', 'Subject', 'Snippet'])  # CSV header


def save_email(sender, subject, snippet):
   
    conn = sqlite3.connect('emails.db')
    c = conn.cursor()
    c.execute('INSERT INTO emails (sender, subject, snippet) VALUES (?, ?, ?)', (sender, subject, snippet))
    conn.commit()
    conn.close()

   
    with open('emails.csv', 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow([sender, subject, snippet])

