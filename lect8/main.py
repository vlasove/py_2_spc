import sqlite3

conn = sqlite3.connect('data.db')
cur = conn.cursor()

query_create = "CREATE TABLE IF NOT EXISTS users (id INT, name TEXT, lastname TEXT, age INT)"
cur.execute(query_create)


#CREATED USER
# UNCOMMENT THIS TO INPUT DATA TO DATABSE
# for i in range(100):
#     user = (i, 'User1', 'Lastname1', int(22*i - 22/(i+1)))
#     query_insert = "INSERT INTO users VALUES(?, ?, ?, ?)"
#     cur.execute(query_insert, user)
#conn.commit()

#READING USER
query_select = "SELECT * FROM users WHERE id > 80"
for row in cur.execute(query_select):
    #print(row)
    pass 

#UPDATING USER
query_update = "UPDATE users SET id = 200 WHERE id > 95"
cur.execute(query_update)
conn.commit()

#DELETING USER 
query_delete = "DELETE FROM users WHERE id = 200"
cur.execute(query_delete)
conn.commit()




conn.close()


#CRUD --- Create - Read - Update - Delete