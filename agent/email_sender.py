import smtplib
from email.message import EmailMessage
import os
from dotenv import load_dotenv

load_dotenv()

def send_email(to_address, subject, content):
    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = os.getenv("EMAIL_ADDRESS")
    msg["To"] = to_address
    msg.set_content(content)

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(os.getenv("EMAIL_ADDRESS"), os.getenv("EMAIL_PASSWORD"))
        smtp.send_message(msg)
