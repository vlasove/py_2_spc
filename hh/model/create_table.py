import sqlite3 

conn = sqlite3.connect('data.db')
cur = conn.cursor()

query = "CREATE TABLE IF NOT EXISTS vacancys (id INTEGER PRIMARY KEY, title TEXT, salary INTEGER)"
cur.execute(query)

conn.close()