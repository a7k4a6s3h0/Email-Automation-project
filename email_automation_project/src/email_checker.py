import imaplib
import email, re
import sys, threading, time

sys.path.append('/path/to/your/project')  # Adjust this path accordingly
# eg : D:\pythonProject29\email_automation_project
from config.config import SMTP_SERVER, SMTP_PORT, SENDER_EMAIL, SENDER_PASSWORD


# validating Email
def is_valid_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email)


# Function to display a loading animation
def loading_animation():
    while email_fetching_thread.is_alive():
        sys.stdout.write('\rEmail Fetching ... |')
        time.sleep(0.1)
        sys.stdout.write('\rEmail Fetching ... /')
        time.sleep(0.1)
        sys.stdout.write('\rEmail Fetching ... -')
        time.sleep(0.1)
        sys.stdout.write('\rEmail Fetching ... \\')
        time.sleep(0.1)
    sys.stdout.write('\rEmail Fetched Successfully!    \n')




def fetch_email(Checking_mail):

    imap_server = "imap.gmail.com"
    imap_port = 993

    with imaplib.IMAP4_SSL(imap_server, imap_port) as mail:
        mail.login(SENDER_EMAIL, SENDER_PASSWORD)
        mail.select("INBOX")
        search_criteria = f"From {Checking_mail}"
        result, data = mail.search(None, search_criteria)

        email_ids = data[0].split()
        if email_ids is None:
            print("No Email Found")
        for email_id in email_ids:
            result, data = mail.fetch(email_id, "(RFC822)")
            raw_email = data[0][1]
            msg = email.message_from_bytes(raw_email)

            # Extract date and time from the email_data
            date_string = msg.get("Date")
            if date_string:
                date = email.utils.parsedate_to_datetime(date_string)
                formatted_date = date.strftime("On %a, %b %d, %Y, %I:%M %p")
            else:
                formatted_date = "Unknown Date"

            print("\nEmail ID:", email_id)
            print("Date:", formatted_date)

            # Extract and print the email body
            for part in msg.walk():
                if part.get_content_type() == "text/plain":
                    body = part.get_payload(decode=True).decode("utf-8")
                    print("Body:" + body)
                    break  # Break to only print the first text/plain part

            print("=" * 40)  # Print a separator between emails

while True:
    Checking_mail = input("Enter Email do you want to check")
    if is_valid_email(Checking_mail):
        break
    print(f"Invalid Email {Checking_mail}")

# Send email to user in a separate thread
email_fetching_thread = threading.Thread(target=fetch_email, args=(Checking_mail,))
email_fetching_thread.start()

# Display loading animation
loading_animation()

# Wait for the email thread to finish
email_fetching_thread.join()

# We use the mail.fetch command with (RFC822) to fetch the complete email message in its raw format.
#
# We create an email.message.Message object (msg) from the raw email data.
#
# We extract the Date header from the msg object and parse it to obtain the formatted date.
#
# We then iterate through the parts of the email message using msg.walk() and look for parts with the content type "text/plain", which typically represents the plain text body of the email.
#
# We decode the payload of the plain text part and print the email body content.
#
# We use a separator (= characters) between each printed email for better readability.
#
# This code should correctly fetch and print the body of each email along with the email ID and date.
