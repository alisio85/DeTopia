from .database import create_connection

def change_user_role(username, new_role):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('UPDATE users SET role = ? WHERE username = ?', (new_role, username))
    conn.commit()
    conn.close()
    return "User role updated successfully."
