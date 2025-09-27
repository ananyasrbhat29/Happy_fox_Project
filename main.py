from gmail_service import get_gmail_service
from database import init_db, save_email

def main():
    init_db()
    service = get_gmail_service()
    results = service.users().messages().list(userId='me', maxResults=200).execute()
    messages = results.get('messages', [])
    
    for msg in messages:
        msg_data = service.users().messages().get(userId='me', id=msg['id']).execute()
        snippet = msg_data.get('snippet', '')
        headers = msg_data['payload']['headers']
        subject = next((h['value'] for h in headers if h['name'] == 'Subject'), '')
        sender = next((h['value'] for h in headers if h['name'] == 'From'), '')
        save_email(sender, subject, snippet)
        print(f"Saved: {subject}")

if __name__ == "__main__":
    main()
