from flask import Blueprint, render_template, request, redirect, url_for, session
import sqlite3
from datetime import datetime
from .models import DATABASE

main = Blueprint('main', __name__)

@main.route('/')
def home():
    if 'username' in session:
        return redirect(url_for('main.dashboard'))
    return render_template('login.html')

@main.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        with sqlite3.connect(DATABASE) as conn:
            c = conn.cursor()
            c.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
            user = c.fetchone()
            if user:
                session['username'] = username
                session['user_id'] = user[0]
                return redirect(url_for('main.dashboard'))
    return render_template('login.html')

@main.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('main.home'))

@main.route('/dashboard')
def dashboard():
    if 'username' not in session:
        return redirect(url_for('main.login'))
    return render_template('dashboard.html', username=session['username'])

@main.route('/log', methods=['GET', 'POST'])
def log_task():
    if 'username' not in session:
        return redirect(url_for('main.login'))
    if request.method == 'POST':
        task = request.form['task']
        date = datetime.now().strftime('%Y-%m-%d')
        with sqlite3.connect(DATABASE) as conn:
            c = conn.cursor()
            c.execute("INSERT INTO tasks (user_id, task, date) VALUES (?, ?, ?)",
                      (session['user_id'], task, date))
        return redirect(url_for('main.dashboard'))
    return render_template('log_task.html')
