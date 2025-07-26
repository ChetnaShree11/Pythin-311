#Devlop a class called text reader which works as follows
class text_reader:
    def __init__(self,fname):
        self.f=fname
        fo=open(fname,'r')
        self.text=fo.read()
        self.lines=len(self.text.split('\n'))
        self.wordcount=len(self.text.split(' '))
        self.word=set(self.text.split(' '))

    def display(self):
        print(self.text)
        print(self.lines)
    def wordlist(self):
        print(self.wordcount)
        print(list(self.word))
    def getWC(self,words):
        d={}        
        for word in words:
            c=self.text.count(word)
            d[word]=c
        
        print(d)
    def save(self):
        f1=open('file2.txt','w')
        f1.write(self.text)
        f1.close()
        
    def replace(self):
        f2=open('article.txt','r+')
        f2.write(self.text.replace("Hello","Hii"))
        f2.seek(0)
        print(f2.read())
        f2.close()
    def add(self):
        f2=open('article.txt','a')
        f2.write('hello')
        f2.close()
        
        
        
    
        
t=text_reader('article.txt')
t.display()
t.wordlist()
l=[]
n=int(input("How many words you need to enter"))
for i in range(0,n):
    wor=input("Enter a word you need count of")
    l.append(wor)
d=t.getWC(l)
t.save()
t.replace()
t.add()




