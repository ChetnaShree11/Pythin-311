import sqlite3
d=sqlite3.connect('words_count.sqlite3')
c=d.cursor()
c.execute('Drop table if exists Words')
c.execute('Create table Words(Word text,counts number)')
print("Words table created")
a=input("Enter the file name")
fo=open(a,'r')
text=fo.read()
dic={}        
for w in text.split(' ') :
    cn=text.count(w)
    dic[w]=cn
    
for x,y in dic.items():
    c.execute("Insert into Words(Word,counts)values(?,?)",(x,y))
d.commit()
fo.close()
c.execute("""SELECT * FROM Words order by counts""")
for row in c:
    print(row)
b=input("Enter a word you need count of")
q=SELECT * FROM Words where Word=?
c.execute(q,(b,))
rec=c.fetchall()
print(rec)
c.execute('SELECT * FROM Words order by Word asc')
for row in c:
    print(row)
d.commit()
