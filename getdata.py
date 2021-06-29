import sqlite3 as sql
import pandas as pd
conn = sql.connect('Guardian.db')

# # for row in conn.execute(f"select * from newstable"):
# # 			print(row)
# cor=conn.cursor()
# cor.execute(f"select * from newstable")
# cor.fetchall()

# data = pd.read_sql_table('newstable', 'postgres:///Guardian.db')
# print(data)
con = sql.connect("Guardian.db")
df = pd.read_sql_query("SELECT * from newstable", con)

# Verify that result of SQL query is stored in the dataframe
print(df)

con.close()