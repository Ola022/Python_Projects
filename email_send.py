import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

""" 6 5	"""
sender_password = "mypassword"
sender_email = "myemail@gmail.com"
receive_email = "doyecov734@mposhop.com"
#receive_email = "abdulazeezabdullateef2021@gmail.com"


""" 
def send_email(to: str, message: str):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(sender_email, sender_password)
    server.sendmail(sender_email, to, message)
    server.close()
    print(sender_email)
"""
# send_email("abdulazeezabdullateef2021@gmail.com", "Horlam Says Hy!")


# Create the email content
subject = "Test Email"
body = "This is a test email sent from Python!"

# Create the email message
msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = receive_email
msg['Subject'] = subject
msg.attach(MIMEText(body, 'plain'))

try:
    # Connect to the SMTP server
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()  # Secure the connection

    # Login to the email account
    server.login(sender_email, sender_password)

    # Send the email
    server.send_message(msg)
    print("Email sent successfully!")

except Exception as e:
    print(f"Failed to send email: {e}")


finally:
    # Disconnect from the server if connected
    try:
        server.quit()
    except NameError:
        pass


