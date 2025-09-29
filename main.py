from gmail_service import get_gmail_service
from database import init_db, save_email

def main():
    init_db()
    print("✅ Database initialized.")

    service = get_gmail_service()
    print("✅ Gmail service initialized.")

   
    results = service.users().messages().list(userId='me', maxResults=50).execute()
    messages = results.get('messages', [])

    if not messages:
        print("No emails found.")
        return

    for msg in messages:
        msg_data = service.users().messages().get(userId='me', id=msg['id']).execute()
        snippet = msg_data.get('snippet', '')
        headers = msg_data['payload']['headers']

        subject = next((h['value'] for h in headers if h['name'] == 'Subject'), '')
        sender = next((h['value'] for h in headers if h['name'] == 'From'), '')

        save_email(sender, subject, snippet, msg['id'])

if __name__ == "__main__":
    main()
