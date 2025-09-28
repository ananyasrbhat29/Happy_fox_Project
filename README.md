# 📧 Gmail Automation Project

This is a standalone Python backend script that integrates with the **Gmail API** to:

- Fetch emails from your Gmail inbox  
- Save them in a **SQLite database** and **CSV file**  
- Process them based on custom rules (like mark read/unread or move message)  

---

## **Project Structure**

| File | Description |
|------|-------------|
| `main.py` | The main entry point of the application. |
| `gmail_service.py` | Handles authentication and interaction with Gmail's API. |
| `database.py` | Manages database operations for storing and retrieving email data. |
| `process_rules.py` | Contains logic for processing emails based on predefined rules. |
| `rules.json` | A JSON file defining the rules for email processing. |
| `emails.db` | SQLite database file storing email information. |
| `emails.csv` | CSV file containing email data. |
| `credentials.json` | OAuth 2.0 credentials for accessing Gmail API. |
| `token.pickle` | Stores the user's access and refresh tokens for Gmail API authentication. |

---

## **Installation**

1. Clone the repository (or copy the project files).  
2. Install dependencies using:

```bash
pip install -r requirements.txt
