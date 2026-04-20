
import MySQLdb
conn=MySQLdb.connect(
	host='localhost',
	user='testuser',
	passwd='abcdef',
	db='testuser',
	charset='utf8'
)

cursor=conn.cursor()