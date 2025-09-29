# 📧 Gmail Automation Project

This is a standalone Python backend script that integrates with the **Gmail API** to:

- Fetch emails from your Gmail inbox  
- Save them in a **SQLite database** and **CSV file**  
- Process them based on custom rules (like mark read/unread or move message)  

---

## Project Files

- `main.py` – The main entry point of the application.  
- `gmail_service.py` – Handles authentication and interaction with Gmail's API.  
- `database.py` – Manages database operations for storing and retrieving email data.  
- `process_rules.py` – Contains logic for processing emails based on predefined rules.  
- `rules.json` – A JSON file defining the rules for email processing.  
- `emails.db` – SQLite database file storing email information.  
- `emails.csv` – CSV file containing email data.  
- `credentials.json` – OAuth 2.0 credentials for accessing Gmail API.  
- `token.pickle` – Stores the user's access and refresh tokens for Gmail API authentication.  

---

## Installation

1. Clone the repository (or copy the project files).  
2. Install dependencies using:

```pip install -r requirements.txt```

# Running the Application

### 1. Fetch and save emails
```python main.py```

### 2. Process emails based on rules
```python process_rules.py```
# Gmail Automation Project

You can access the demonstration video and the presentation, through the following Google Drive link:

👉 [Gmail Automation Project Files](https://drive.google.com/drive/folders/16PKT65asEvmFDfnx8XW5h_lcAtE2mx_d?usp=drive_link)

> **IMPORTANT — credentials.json (DUMMY DATA)**
>
> The `credentials.json` file included here contains **dummy placeholder values only** and must be **replaced** with your own OAuth credentials downloaded from Google Cloud Console.  
> **Do NOT** use the dummy values for production or real accounts — committing or sharing real credentials can cause serious security and billing issues.




