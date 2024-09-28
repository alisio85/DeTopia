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
            email TEXT,
            resources TEXT  -- Nuova colonna per gestire le risorse
        )
    ''')
    conn.commit()
    conn.close()

def reset_database():
    if os.path.exists('users.db'):
        os.remove('users.db')
    create_table()

def register_user(username, password, email, role='user'):
    conn = create_connection()
    cursor = conn.cursor()
    try:
        cursor.execute('INSERT INTO users (username, password, role, email, resources) VALUES (?, ?, ?, ?, ?)', 
                       (username, password, role, email, '[]'))  # Inizializza le risorse come una lista vuota
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
    """Aggiorna le risorse dell'utente."""
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('UPDATE users SET resources = ? WHERE username = ?', (resources, username))
    conn.commit()
    conn.close()
