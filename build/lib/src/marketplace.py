from .database import create_connection

def add_item_to_marketplace(item_name, price):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO marketplace (item_name, price) VALUES (?, ?)', (item_name, price))
    conn.commit()
    conn.close()
    return "Item added to marketplace."
