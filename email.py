#import classes so that we dont need to use a full module name later
import smtplib, ssl

port = 465 # For SSL
password = input ("Type your password and press enter: ")

#create a secure ssl context
context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    server.login("my@gmail.com", password)
    # TODO: Send email here

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


sender_email = "your@gmail.com"
receiver_email = "recepient@gmail.com"
password = input("Type password and press enter:")

message = MIMEMultipart("alternative")
message ["Subject"] = "multipart test"
message ["From"] = sender_email
message ["To"] = receiver_email

#create the plain-text and HTML version of your message
text = """\
    Hi,
    How have you been?
    Check out my GitHub:
    https://github.com/KamilKalowski"""
html = """\
        <html>
            <body>
                <p>Hi, <br>
                    How have you been? <br>
                    <a href="https://github.com/KamilKalowski"> Check out </a>
                    my GitHub.
                </p>
            </body>
        </html>
        """

#turn these into plain/html MIMEText objects
part1 = MIMEText(text, "plain")
part2 = MIMEText(html, "html")

#add html/plain-text parts to MIMEMultipart message
#the email client will try to render last part first
message.attach(part1)
message.attach(part2)

#create secure connection with server with server and send email
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(
        sender_email, receiver_email, message.as_string()
    )