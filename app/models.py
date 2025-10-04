import sqlite3

DATABASE = 'activity_logger.db'

def init_db():
    with sqlite3.connect(DATABASE) as conn:
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS users (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        username TEXT UNIQUE NOT NULL,
                        password TEXT NOT NULL,
                        email TEXT NOT NULL
                    )''')
        c.execute('''CREATE TABLE IF NOT EXISTS tasks (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        user_id INTEGER,
                        task TEXT,
                        date TEXT,
                        FOREIGN KEY(user_id) REFERENCES users(id)
                    )''')
init_db()
