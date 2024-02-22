import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

def send_email(sender_email, sender_password, recipients, subject, body, attachment_path=None):
    try:
        # Create message container - the correct MIME type is multipart/alternative.
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = ', '.join(recipients)
        msg['Subject'] = subject

        # Attach body
        msg.attach(MIMEText(body, 'plain'))

        # Attach attachment if provided
        if attachment_path:
            with open(attachment_path, "rb") as attachment:
                part = MIMEBase('application', 'octet-stream')
                part.set_payload(attachment.read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', f'attachment; filename= {attachment_path}')
            msg.attach(part)

        # Establishing connection with Gmail SMTP server
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(sender_email, sender_password)

        # Sending email
        server.sendmail(sender_email, recipients, msg.as_string())
        print("Email sent successfully!")
    except smtplib.SMTPAuthenticationError:
        print("SMTP authentication error: Please check your email address and password.")
    except smtplib.SMTPException as e:
        print("An error occurred while sending the email:", e)
    finally:
        if 'server' in locals():
            server.quit()

# Change these as per your use
your_email = "praveen.gopi717@gmail.com"
your_password = "wsjb dise wtad bspn"
recipients = ["praveengopi998@gmail.com"]
subject = "Test Email with Attachment"
body = "Hello, world!"
attachment_path = "Praveen_mca_B.jpeg"

# Call the function to send the email
send_email(your_email, your_password, recipients, subject, body, attachment_path)
