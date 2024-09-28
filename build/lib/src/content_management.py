from .database import create_connection

def create_content(title, body, author):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO content (title, body, author) VALUES (?, ?, ?)', (title, body, author))
    conn.commit()
    conn.close()
    return "Content created successfully."
