from .database import create_connection

def create_vote(topic, options):
    conn = create_connection()
    cursor = conn.cursor()
    for option in options:
        cursor.execute('INSERT INTO votes (topic, option) VALUES (?, ?)', (topic, option))
    conn.commit()
    conn.close()
    return "Vote created successfully."

def cast_vote(user, option):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO votes (user, option) VALUES (?, ?)', (user, option))
    conn.commit()
    conn.close()
    return "Vote cast successfully."
