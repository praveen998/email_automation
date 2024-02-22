import smtplib
from email.mime.text import MIMEText

def send_email(sender_email, sender_password, message):
    ack=None
    try:
        # Establishing connection with Gmail SMTP server
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(sender_email, sender_password)
        # Sending email
        server.sendmail(sender_email, ["praveengopi998@gmail.com"], message)
        ack="Email sent successfully!"
        print(ack)
    except smtplib.SMTPAuthenticationError:
        ack="SMTP authentication error: Please check your email address and password."
        print(ack)
    except smtplib.SMTPException as e:
        ack="An error occurred while sending the email:"
        print(ack, e)    
    finally:
        if 'server' in locals():
            server.quit()
    return ack

# Change these as per your use
your_email = "praveen.gopi717@gmail.com"
your_password = "wsjb dise wtad bspn"
message = "Hello, world!"

# Call the function to send the email
send_email(your_email, your_password, message)
