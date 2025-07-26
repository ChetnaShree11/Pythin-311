import sqlite3
d=sqlite3.connect('words_count.sqlite3')
c=d.cursor()
c.execute('Drop table if exists Words')
c.execute('Create table Words(Word text,counts number)')
print("Words table created")
a=input("Enter a sentence")
dic={}        
for w in a.split(' ') :
    cn=a.count(w)
    dic[w]=cn
    
for x,y in dic.items():
    c.execute("Insert into Words(Word,counts)values(?,?)",(x,y))
d.commit()
c.execute('SELECT * FROM Words order by counts')
for row in c:
    print(row)
d.commit()
