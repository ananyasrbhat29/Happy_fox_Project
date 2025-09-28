import json
import sqlite3
from datetime import datetime, timedelta

def apply_rules():
    with open('rules.json') as f:
        rules = json.load(f)
    
    conn = sqlite3.connect('emails.db')
    c = conn.cursor()
    c.execute("SELECT id, sender, subject, snippet FROM emails")
    emails = c.fetchall()

    for email in emails:
        email_id, sender, subject, message = email

        for rule in rules['rules']:
            field_value = ""

           
            if rule['field'] == 'from':
                field_value = sender
            elif rule['field'] == 'subject':
                field_value = subject
            elif rule['field'] == 'message':
                field_value = message
            elif rule['field'] == 'received_date':
               
                continue

            value = rule['value'].lower()
            field_value = field_value.lower()

          
            match = False
            if rule['predicate'] == 'contains' and value in field_value:
                match = True
            elif rule['predicate'] == 'does_not_contain' and value not in field_value:
                match = True
            elif rule['predicate'] == 'equals' and value == field_value:
                match = True
            elif rule['predicate'] == 'does_not_equal' and value != field_value:
                match = True

           
            if match:
                for action in rule['actions']:
                    print(f"✅ Action '{action}' triggered for email '{subject}'")

    conn.close()

if __name__ == "__main__":
    apply_rules()

