#Build a list of numbers in a text file
f=input("Enter the file name")
try:
    fo=open(f,'r')
    r=fo.read()
except:
    print("No such file found")
else:
    l=[]
    for i in r:
        if (i.isdigit()):
            l.append(i)
    print(l)
