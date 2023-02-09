import smtplib
import fire

def send_email(sender_email, receiver_email, subject, message):
    password_app="YOUR_PASS_APP"
    message = f"Subject: {subject}\n\n{message}"
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(sender_email, password_app)
    server.sendmail(sender_email, receiver_email, message)
    server.quit()

if __name__ == '__main__':
    fire.Fire({
      'send': send_email,
    })



