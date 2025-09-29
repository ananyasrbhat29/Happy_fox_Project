import json
import sqlite3
from gmail_service import get_gmail_service  

def apply_rules():
    # Load rules
    with open('rules.json') as f:
        rules = json.load(f)

    
    conn = sqlite3.connect('emails.db')
    c = conn.cursor()
    c.execute("SELECT gmail_id, sender, subject, snippet FROM emails")
    emails = c.fetchall()

    
    service = get_gmail_service()

    for email in emails:
        gmail_id, sender, subject, message = email

        for rule in rules['rules']:
            field_value = ""

            
            if rule['field'] == 'from':
                field_value = sender
            elif rule['field'] == 'subject':
                field_value = subject
            elif rule['field'] == 'message':
                field_value = message
            else:
                continue  

           
            rule_value = rule['value'].strip().lower()
            email_value = field_value.strip().lower()

            
            match = False
            if rule['predicate'] == 'contains':
                match = rule_value in email_value
            elif rule['predicate'] == 'does_not_contain':
                match = rule_value not in email_value
            elif rule['predicate'] == 'equals':
                match = email_value == rule_value
            elif rule['predicate'] == 'does_not_equal':
                match = email_value != rule_value

            if match:
                print(f"✅ Matched rule: {rule['predicate']} '{rule_value}' with email '{email_value}'")

               
                for action in rule['actions']:

                    if action == "mark_unread":
                        try:
                            service.users().messages().modify(
                                userId='me',
                                id=gmail_id,
                                body={"addLabelIds": ["UNREAD"]}
                            ).execute()
                            print(f"🙈 Marked '{subject}' as UNREAD")
                        except Exception as e:
                            print(f"❌ Failed to mark '{subject}' as UNREAD: {e}")

                    elif action == "mark_read":
                        try:
                            service.users().messages().modify(
                                userId='me',
                                id=gmail_id,
                                body={"removeLabelIds": ["UNREAD"]}
                            ).execute()
                            print(f"👁 Marked '{subject}' as READ")
                        except Exception as e:
                            print(f"❌ Failed to mark '{subject}' as READ: {e}")

                    elif action.startswith("move:"):
                        try:
                            label_id = action.split(":")[1]
                            service.users().messages().modify(
                                userId='me',
                                id=gmail_id,
                                body={"addLabelIds": [label_id], "removeLabelIds": ["INBOX"]}
                            ).execute()
                            print(f"📂 Moved '{subject}' to label {label_id}")
                        except Exception as e:
                            print(f"❌ Failed to move '{subject}': {e}")

                    elif action == "delete":
                        try:
                            service.users().messages().delete(
                                userId='me',
                                id=gmail_id
                            ).execute()
                            print(f"🗑 Deleted email '{subject}'")
                        except Exception as e:
                            print(f"❌ Failed to delete '{subject}': {e}")

    conn.close()

if __name__ == "__main__":
    apply_rules()
