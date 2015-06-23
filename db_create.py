import sqlite3
import os
#import pdb
from _config import DATABASE_PATH

with sqlite3.connect(DATABASE_PATH) as connection:
	c = connection.cursor()

	c.execute(
			  """
				CREATE TABLE subsunday(id INTEGER PRIMARY KEY AUTOINCREMENT,
				username TEXT NOT NULL, choice TEXT NOT NULL, weektotal INTEGER
				NOT NULL, weekdate DATE)
			  """
			 )

def insertdata(folder):
	with sqlite3.connect(DATABASE_PATH) as connection:
		connection.text_factory = str
		c = connection.cursor()
		for filename in os.listdir(folder):
			votedate = filename[11:21]
			with open((str(folder)+ '/' +str(filename)), 'r') as currentdoc:
				totalvotes = currentdoc.read()[17:21]
			#pdb.set_trace()
			with open((str(folder)+ '/' +str(filename)), 'r') as currentdoc:
				next(currentdoc)
				for line in currentdoc:
					username = line[0:line.find('-')-1]
					choice = line[len(username) + 3:]
					docdata = (str(username), str(choice), int(totalvotes), str(votedate))
					c.execute("INSERT INTO subsunday(username, choice, weektotal, weekdate) VALUES(?,?,?,?)", docdata)

# Populates database with the contents of choosen folder
insertdata('ssdata')