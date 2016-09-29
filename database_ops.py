import MySQLdb

class database:
	def __init__(self, ID='shubham', pass='shubh1234', database='news_classifier', hst='localhost'):
		self.userID=ID
		self.password=pass
		self.dbase=database
		self.host=hst

		try:
			self.db=MySQLdb.connect(self.host, self.userID, self.password, self.database)
			print 'Connected to Database'
		except:
			print "Could not connect to database"

	def __del__():
		db.close()

	def create_new_table(self):
		cursor=self.db.cursor()
		sql_command='''CREATE TABLE BOW(
					WORD VARCHAR(50),
					FREQ INT, 
					PRIMARY KEY(WORD)
					)'''
		try:
			cursor.execute(sql_command)
			print 'Created table'
		except:
			print "Couldn't create table"
		finally:
			cursor.close()

	def add_to_table(self, word_dict):
		cursor=self.db.cursor();
		sql_command='''INSERT into BOW values (''' +word + ''',''' + str(count) + ")"
		try:
			cursor.execute(sql_command)
			print 'added word to db'
			self.db.commit()
		except:
			'print error adding word'
		finally:
			cursor.close()



	def add_to_database():
    	return 1