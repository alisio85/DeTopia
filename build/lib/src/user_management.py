import sqlite3
import os

def create_connection():
    conn = sqlite3.connect('users.db')
    return conn

def create_table():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            username TEXT PRIMARY KEY,
            password TEXT,
            role TEXT,
            email TEXT
        )
    ''')
    conn.commit()
    conn.close()

def reset_database():
    if os.path.exists('users.db'):
        os.remove('users.db')
    create_table()

def register_user(username, password, role='user', email=''):
    conn = create_connection()
    cursor = conn.cursor()
    try:
        cursor.execute('INSERT INTO users (username, password, role, email) VALUES (?, ?, ?, ?)', (username, password, role, email))
        conn.commit()
        return "User registered successfully."
    except sqlite3.IntegrityError:
        return "Username already exists."
    finally:
        conn.close()

def login_user(username, password):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT password FROM users WHERE username = ?', (username,))
    row = cursor.fetchone()
    conn.close()
    if row is None:
        return "User does not exist."
    if row[0] != password:
        return "Invalid password."
    return "Login successful."

def get_user_role(username):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT role FROM users WHERE username = ?', (username,))
    row = cursor.fetchone()
    conn.close()
    if row is None:
        return "User does not exist."
    return row[0]

def update_user_resources(username, resources):
    # Funzione per aggiornare le risorse dell'utente (da implementare)
    pass

