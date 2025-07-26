#Write a program to accept file name from the user and display all the lines containing "Subject" as first word
f=input("Enter the file name")
fo=open(f)
count=0
for i in fo:
    if i.startswith("Subject"):
        count+=1
print("Number of lines containing Subject=",count)
fo.close()        
