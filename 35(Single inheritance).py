#Single level inheritance
class person():
    def __init__(self):
        self.name=""
        self.ph=""
        self.DOB=""
        self.ad=""
        
    def display(self):
        print("Name=",self.name)
        print("Adress=",self.ad)
        print("Phone number=",self.ph)
        print("Date of birth=",self.DOB)
    def get_data(self):
        self.name=input("Enter name")
        self.ph=input("Enter Phone number")
        self.DOB=input("Enter date of Birth")
        self.ad=input("Enter your adress")
        
        

class student(person):
    def __init__(self):
        person. __init__(self)
    def display_stu(self):
        print("Roll number=",self.R)
        print("Class=",self.C)
    def get_studata(self):
        self.R=input("Enter your Roll number")
        self.C=input("Enter your class")
s=student()
s.get_data()
s.get_studata()
print('*'*25)
s.display()
s.display_stu()
