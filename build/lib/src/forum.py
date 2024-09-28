from .database import create_connection

def post_message(username, message):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO forum_posts (username, message) VALUES (?, ?)', (username, message))
    conn.commit()
    conn.close()
    return "Message posted to forum."
