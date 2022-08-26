from email.message import EmailMessage
import ssl
import smtplib
import mimetypes
import os
from os.path import basename



email_sender = 'adekeyedamola72@gmail.com'
email_password = 'jwnotsctzsaxgeli'
email_receiver = 'adekeyedamola72@gmail.com'
subject = 'This is a test'
body = """
This is a test of how to send an email address using python.
My name is Adedamola. I am software developer in Adroit Solutions Ltd. 
I am relentless.
I am prudent.
I will accomplish all my goals.
I just need TIME  :)
"""

message = EmailMessage()
message['From'] = email_sender
message['To'] = email_receiver
message['Subject'] = subject
message.set_content(body)

attachment_path = "C:\\Users\\user\\Desktop\\Adroit\\Book1.xlsx"
attachment_filename = os.path.basename(attachment_path)

mime_type, _ = mimetypes.guess_type(attachment_path)


mime_type, mime_subtype = mime_type.split('/', 1)


with open(attachment_path, 'rb') as ap:
    message.add_attachment(ap.read(), maintype=mime_type, subtype=mime_subtype, filename=os.path.basename(attachment_path))

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as mail_server:
    mail_server.login(email_sender, email_password)
    mail_server.send_message(message)
    mail_server.quit()