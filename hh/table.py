import sqlite3

conn = sqlite3.connect('data.db')
cur = conn.cursor()

query = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)"
cur.execute(query)

user1 = ('Bob', 22)
user2 = ('Jack', 33)

query_insert = "INSERT INTO users VALUES(NULL, ?, ?)"
cur.execute(query_insert, user1)
cur.execute(query_insert, user2)

conn.commit()

conn.close()
