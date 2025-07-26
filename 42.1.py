#Adding entries
import sqlite3
a=sqlite3.connect('music.sqlite3')
b=a.cursor()
b.execute('DROP TABLE IF EXISTS Writers')
b.execute('CREATE TABLE Writers(ID NUMBER PRIMARY KEY,NAME TEXT)')
print("Writers table created")
b.execute('INSERT INTO WRITERS(ID,NAME)VALUES(1,"Jack London")')
b.execute('INSERT INTO WRITERS(ID,NAME)VALUES(2,"Honore De Balzao")')
b.execute('INSERT INTO WRITERS(ID,NAME)VALUES(3,"Lion Feuchtwanger")')
b.execute('INSERT INTO WRITERS(ID,NAME)VALUES(4,"Emilie Zola")')
b.execute('INSERT INTO WRITERS(ID,NAME)VALUES(5,"Truman Capote")')
a.commit()
b.execute('SELECT * FROM Writers WHERE(Id<5)')
for row in b:
    print(row)
b.execute('UPDATE writers SET Name="Chetna" WHERE Id=4')
print("Updated data:")
b.execute('SELECT * FROM Writers WHERE(Id<=5)')
for row in b:
    print(row)
a.commit()
a.close()
