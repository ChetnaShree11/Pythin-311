#Read a text file and convert it into uppercase and write it to a second file
f=input("Enter the file name")
fo=open(f,'r')
f1=(fo.read()).upper()
print(f1)
fo.close()

f2=input("Enter the file where you want to copy the content")
f3=open(f2,'w')
f3.write(f1)
f3.close()
