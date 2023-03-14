import sqlite3

db_name = "quotes_db"
table_name = "quotes"
conn = sqlite3.connect(db_name)
cursor = conn.cursor()

def init_db():
    table_sql = f"""CREATE TABLE IF NOT EXISTS {table_name} (
                quote text,
                author text
                )"""
    cursor.execute(table_sql)
    cursor.close()
    conn.close()


def open_conn():
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()


def close_conn():
    cursor.close()
    conn.close()


def add_row(quote):
    open_conn()
    cursor.execute('INSERT INTO quotes VALUES (:quote, :author)',{'quote': quote.text, 'author': quote.author})
    conn.commit()
    close_conn()


def get_quotes():
    open_conn()
    cursor.execute(f'select * from {table_name}')
    results = cursor.fetchall()
    quote_list = []
    for result in results:
        quote_list.append(result)
    return quote_list