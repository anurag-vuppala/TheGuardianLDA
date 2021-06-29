import sqlite3 as sql
conn = sql.connect('Guardian.db')

conn = sql.connect('Guardian.db')
for row in conn.execute(f"select * from newstable"):
			print(row)
