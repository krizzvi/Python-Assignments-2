import smtplib
from email.mime.text import MIMEText

def send_emails():
    with open("contacts.txt") as f:
        for line in f:
            name, email = line.strip().split(",")
            msg = MIMEText(f"Hello {name}, this is a test email.")
            msg["Subject"] = "Test Email"
            msg["From"] = "you@example.com"
            msg["To"] = email

            print(f"Sending to {email}...")
            try:
                # Uncomment and configure below for actual sending
                # with smtplib.SMTP("smtp.example.com") as server:
                #     server.login("your_username", "your_password")
                #     server.send_message(msg)
                print(f"Email to {email} sent (mock).")
            except Exception as e:
                print(f"Error sending to {email}: {e}")

def main():
    send_emails()

if __name__ == "__main__":
    main()