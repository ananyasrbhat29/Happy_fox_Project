📧 Gmail Automation Project
This is a standalone Python backend script that integrates with the Gmail API to:
Fetch emails from your Gmail inbox
Save them in a SQLite database and CSV file
Process them based on custom rules (like mark read/unread or move message)


The project contains the following files:  

1.main.py: The main entry point of the application.
2.gmail_service.py: Handles authentication and interaction with Gmail's API.
3.database.py: Manages database operations for storing and retrieving email data.
4.process_rules.py: Contains logic for processing emails based on predefined rules.
5.rules.json: A JSON file defining the rules for email processing.
6.emails.db: SQLite database file storing email information.
7.emails.csv: CSV file containing email data.
8.credentials.json: OAuth 2.0 credentials for accessing Gmail API.
9.pickle: Stores the user's access and refresh tokens for Gmail API authentication.


Install Dependencies:
pip install -r requirements.txt

 
Obtain Gmail API Credentials:
Visit the Google Cloud Console
Create OAuth 2.0 credentials and download the credentials.json file.


Run the Application:
python main.py
run process_rules.py
