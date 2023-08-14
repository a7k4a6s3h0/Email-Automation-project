import re
import sys
import time
import sys
import threading
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

sys.path.append('D:\pythonProject29\email_automation_project')  # Adjust this path accordingly
from config.config import SMTP_SERVER, SMTP_PORT, SENDER_EMAIL, SENDER_PASSWORD

# create email to user

Warning_msg = '''To Sent Email To User You Need To Fill Some Details (Receiver Email, Subject, Message)'''
print('#' * 4 + ' ' + Warning_msg + ' ' + '#' * 4)

# Dictionary to store User Data
provided_data = {}


# validating Email
def is_valid_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email)


# Function to display a loading animation
def loading_animation():
    while email_thread.is_alive():
        sys.stdout.write('\rSending email ... |')
        time.sleep(0.1)
        sys.stdout.write('\rSending email ... /')
        time.sleep(0.1)
        sys.stdout.write('\rSending email ... -')
        time.sleep(0.1)
        sys.stdout.write('\rSending email ... \\')
        time.sleep(0.1)
    sys.stdout.write('\rEmail sent successfully!    \n')


provided_data['receiver_email'] = ''
provided_data['subject'] = ''
provided_data['message'] = ''

missing_key = [key for key, value in provided_data.items() if value == ""]
if missing_key:
    for index, item in enumerate(missing_key):
        if item in provided_data:
            while True:
                # print(f"You Need To Provide {item}\n")
                provided_data[item] = input(f"Enter {item}")
                if item == 'receiver_email':
                    if is_valid_email(provided_data[item]) is None:
                        print(f"It's Not a Valid Email {provided_data[item]}")
                        continue
                if provided_data[item] == "":
                    continue
                break
missing_key = None
print(provided_data)
command = input("Do you want to Procide ? (yes: y / no: N)\n")
if command.upper() == 'N':
    quit()


# send email to user
def send_email(provided_data):
    msg = MIMEMultipart()
    msg['From'] = SENDER_EMAIL
    msg['To'] = provided_data['receiver_email']
    msg['Subject'] = provided_data['subject']
    msg.attach(MIMEText(provided_data['message'], 'plain'))

    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()  # Secure the connection
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.sendmail(SENDER_EMAIL, provided_data['receiver_email'], msg.as_string())


# Send email to user in a separate thread
email_thread = threading.Thread(target=send_email, args=(provided_data,))
email_thread.start()

# Display loading animation
loading_animation()

# Wait for the email thread to finish
email_thread.join()
