from flask import Flask
from flask_mail import Mail
from apscheduler.schedulers.background import BackgroundScheduler
from .routes import main
from .email_scheduler import send_weekly_summary
import os

app = Flask(__name__)
app.config.from_object('config.Config')

mail = Mail(app)
app.register_blueprint(main)

scheduler = BackgroundScheduler()
scheduler.add_job(func=send_weekly_summary, trigger='cron', day_of_week='sat', hour=18)
scheduler.start()
