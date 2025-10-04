import sqlite3
from flask_mail import Message
from datetime import datetime, timedelta
from .models import DATABASE
from . import app, mail

def send_weekly_summary():
    with sqlite3.connect(DATABASE) as conn:
        c = conn.cursor()
        c.execute("SELECT id, username, email FROM users")
        users = c.fetchall()
        for user_id, username, email in users:
            c.execute("SELECT task, date FROM tasks WHERE user_id=? AND date >= ?",
                      (user_id, (datetime.now() - timedelta(days=7)).strftime('%Y-%m-%d')))
            tasks = c.fetchall()
            if tasks:
                body = f"Weekly Summary for {username}:

"
                for task, date in tasks:
                    body += f"- {date}: {task}
"
                msg = Message(subject=f"Weekly Summary - {username}",
                              sender=app.config['MAIL_USERNAME'],
                              recipients=['manager_email@example.com'],
                              body=body)
                mail.send(msg)
