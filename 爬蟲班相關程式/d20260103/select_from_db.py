import MySQLdb
try:
	conn=MySQLdb.connect(
		host='localhost',
		user='testuser',
		passwd='abcdef',
		db='testuser',
		charset='utf8mb4'
	)

	cursor=conn.cursor()
	print("connect successfully")
except MySQLdb.Error as e:
	print("Error")
	print("Wrong message:",e)

sql="SELECT name,math FROM studenttab WHERE math>=90;"
cursor.execute(sql)
rows=cursor.fetchall()
for r in rows:
	print(r)