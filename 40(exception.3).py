#Display all the line numbers containing any digit
f=input("Enter the file name")
try:
    fo=open(f,'r')
    r=fo.read()
except FileNotFoundError:
    print("No such file found")
else:
    count=0
    for i in r:
        if (i.isdigit()):
            count+=1
    print(count)
