


import smtplib
from email.mime.text import MIMEText

email_sender = "botkumar125@gmail.com"
email_pwd = "botjith125"
email_recipient = "chvenbalasubramanyam@gmail.com"

def send_email():

    subject = "unauthorized access attempt"
    body = " someone with unregistered number is attempting to access"
    message = MIMEText(body)
    message['Subject'] = subject
    message['From'] = email_sender
    message['To'] = email_recipient

    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(email_sender, email_pwd)
        server.sendmail(email_sender, email_recipient, message.as_string())


send_email()