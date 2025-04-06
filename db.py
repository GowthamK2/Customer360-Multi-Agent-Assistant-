import sqlite3

def init_db():
    conn = sqlite3.connect('customers.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS customers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            email TEXT,
            account_type TEXT,
            location TEXT
        )
    ''')

    conn.commit()
    conn.close()

def add_customer(name, email, account_type, location):
    conn = sqlite3.connect('customers.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO customers (name, email, account_type, location) VALUES (?, ?, ?, ?)',
                   (name, email, account_type, location))
    conn.commit()
    conn.close()

def get_all_customers():
    conn = sqlite3.connect('customers.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM customers')
    results = cursor.fetchall()
    conn.close()
    return results
