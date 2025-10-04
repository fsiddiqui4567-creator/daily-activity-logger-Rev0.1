def send_weekly_summary():
    from app import app, mail
    from flask_mail import Message

    with app.app_context():
        msg = Message(
            subject="Weekly Summary",
            sender=app.config['MAIL_USERNAME'],
            recipients=["recipient@example.com"],  # Replace with actual recipient(s)
            body="This is your weekly summary email."
        )
        mail.send(msg)
        print("Weekly summary email sent.")