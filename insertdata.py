# from createdatabase import Data_handle
import pandas as pd
import sqlite3 as sql
# data = pd.read_pickle('data.pickle')
# # print(data)

count=0
conn = sql.connect('Guardian.db')
for row in conn.execute(f"select * from newstable"):
			print(row)
			count=count+1		
print(count)
# a = cur.execute("""select * from album""")

'''
d = Data_handle("bigbb")

print(d.insert_data("bigbb","afaifuagsofa","aaias","jytdsyt.com"))

d.display("bigbb")

'''
# conn = sq.connect('delete.db')

# c = conn.cursor()
# c.execute('''CREATE TABLE delete (
#  			Headline text,
#  			Summery text,
#  			Link integer
# 			)''')


# for newss, heads, links in data[0,:],:2
# 	news = newss
# 	head  = heads
# 	link = links
# 	print(news,heads,links)
# 	c.execute('''INSERT INTO name values (?, ?, ?)''', (news, head, link))
# 	print("Valuse Inserted")
# 	conn.commit()
# # conn.close()
# for i in range(data):
# 	print(i)
# print(data)