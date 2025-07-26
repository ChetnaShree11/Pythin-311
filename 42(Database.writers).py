#Create a table Writers
import sqlite3
a=sqlite3.connect('music.sqlite3')
b=a.cursor()
b.execute('DROP TABLE IF EXISTS Writers')
b.execute('CREATE TABLE Writers(ID NUMBER PRIMARY KEY,NAME TEXT)')
print("Writers table created")
a.close()
