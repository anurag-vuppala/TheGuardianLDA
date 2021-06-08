import sqlite3 as sq
from scrap import data

class Data_handle:

	def __init__(self, table_name):
		self.table = table_name
		try:
			conn = sq.connect('data.db')
			c =  conn.cursor()
			c.execute(f"create table {self.table}(headline text, summery text, links text)")
			conn.commit()
			conn.close()
			print('table created')
		except:
			print("table already exist")
				
		


	def insert_data(self, table_name, news, head, link):
		conn = sq.connect('data.db')
		c =  conn.cursor()
		c.execute(f"INSERT INTO {table_name}(headline, summery, links) values ('{head}','{news}','{link}')")
		conn.commit()
		conn.close()
		return "Values inserted!!!!"



	def display(self, table_name):
		conn = sq.connect('data.db')
		c =  conn.cursor()
		for row in c.execute(f"select * from {self.table}"):
			print(row)
		conn.commit()
		conn.close()	

	
	def custom_command(self, command):
		conn = sq.connect('data.db')
		c =  conn.cursor()
		for row in c.execute(f"{self.command}"):
			print(row)
		conn.commit()
		conn.close()		


print(data)

# for row in c.execute('''SELECT * FROM '''):
#     print(row)


# def create_table(table_name):
	

# 	c.execute(f'''CREATE TABLE {table_name} (
# 			Headline text,
# 			Summery text,
# 			Link integer
# 		)''')

# 	return print('table create!!')		




# def insert_data():
# 	# c.execute(f'''INSERT INTO {table_name} VALUES ('{head}','{summery}','{link}')''')	
# 	c.execute("insert into stu(Headline, Summery, Link) values (?, ?, ?)", persons)
# 	return print('value inserted!')

# create_table("name")	

# insert_data()
# print(c.fetchone())

