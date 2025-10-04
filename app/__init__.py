from flask import Flask
from flask_mail import Mail
from flask_apscheduler import APScheduler
import os

app = Flask(__name__)

# Load configuration from config.py located in the root directory
config_path = os.path.abspath(os.path.join(os.getcwd(), 'config.py'))
app.config.from_pyfile(config_path)

# Initialize Flask-Mail
mail = Mail(app)

# Define the job function
def send_weekly_summary():
    print("Weekly summary email sent.")

# Configure and start APScheduler
class Config:
    SCHEDULER_API_ENABLED = True

app.config.from_object(Config)

scheduler = APScheduler()
scheduler.init_app(app)
scheduler.start()

scheduler.add_job(
    id='WeeklySummaryJob',
    func=send_weekly_summary,
    trigger='cron',
    day_of_week='sat',
    hour=18,
    minute=0
)

# Homepage route
@app.route("/")
def home():
    return "Welcome to the Daily Activity Logger!"
