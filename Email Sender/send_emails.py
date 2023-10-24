import smtplib
from email.message import EmailMessage

sender_email = "my_email@example.com"
sender_password = "my_email_password"

emails = [
    ("John Doe", "john@example.com"),
    ("Jane Doe", "jane@example.com")
]

for name, recipient in emails:
    message = EmailMessage()
    message['From'] = sender_email
    message['To'] = recipient
    message['Subject'] = f"Hi {name}"
    
    message.set_content(f"Hello {name}, hope you are doing well!")
    
    with smtplib.SMTP_SSL('smtp.example.com', 465) as server:
        server.login(sender_email, sender_password)
        server.send_message(message)
        
    print(f"Email sent to {name} at {recipient}")