#load  text from the file
f=input("enter the file name")
try:
    fo=open(f,'r')
except FileNotFoundError:
    s=' '
else:
    s=fo.read()
finally:
    print(s)
