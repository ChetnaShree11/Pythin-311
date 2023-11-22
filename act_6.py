student=[]
def add():
    name=input("Enter student name: ")
    roll=input("Enter Roll number: ")
    marks=input("Enter the marks: ")
    record={'Name': name, 'Roll No.': roll, 'Marks': marks}
    student.append(record)

def search():
    x=input("Enter student Name: ")
    for j in student:
        if j['Name']==x:
            print("Record Found")
            print("Name: ",j['Name'])
            print("Roll No.: ",j['Roll No.'])
            print("Marks: ",j['Marks'])
            
while(1):
    print("1. Add\n2. Search\n3. Exit")
    ch=int(input("Enter your choice: "))
    if ch==1:
        add()
    elif ch==2:
        search()
    elif ch==3:
        break;
