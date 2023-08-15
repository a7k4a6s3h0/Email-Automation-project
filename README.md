
# Email Automation Project

This project implements an email automation system with two main functionalities: sending structured emails and checking for specific incoming emails.


## Features

- Email Sender: The project allows users to send emails with proper structure, including subject, message, and recipient email. It provides validation for the recipient's email address.

- Email Checker: Users can check their inbox for emails from a specific sender email. The project fetches and displays the subject, date, and body of the received emails.

## Prerequisites
- Python 3.x
- smtplib and email libraries (install using pip install secure-smtplib)
- IMAP server access (for email checking)


## Setup and Installation

1) Install my-project with git clone command

```bash
  git clone https://github.com/yourusername/email-automation-project.git

```
2) Then access the project directory
``` bash 
cd email-automation-project
```
3) Install dependencies

```bash
pip install -r requirements.txt
```
4) Configure SMTP and IMAP settings in config.py:

```bash
SMTP_SERVER = 'smtp.example.com'
SMTP_PORT = 587
SENDER_EMAIL = 'your_email@example.com'
SENDER_PASSWORD = 'your_email_password'

# IMAP settings for checking emails
IMAP_SERVER = 'imap.example.com'
IMAP_PORT = 993
```

    
## Usage

### Sending Emails

1) Run email_sender.py:

```bash
python email_sender.py
```

2) Follow the prompts to provide recipient email, subject, and message.

### Checking Emails

1) Run email_checker.py:

```basg
python email_checker.py
```
2) Enter the email address you want to check for.


# Note

- The project includes error handling and validation for email inputs.
- Be cautious with email automation and ensure you have the necessary permissions for accessing SMTP and IMAP servers.
