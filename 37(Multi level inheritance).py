#Multilevel inheritance
class person():
    def __init__(self):
        self.name=""
        self.ph=""
        self.ad=""
        
    def show_person(self):
        print("Name=",self.name)
        print("Adress=",self.ad)
        print("Phone number=",self.ph)
    def get_person(self):
        self.name=input("Enter name")
        self.ph=input("Enter Phone number")
        self.ad=input("Enter your adress")

class employee(person):
    def __init__(self):
        person. __init__(self)
    def show_employee(self):
        print("Employee code=",self.EC)
        print("Salary=",self.S)
        
    def get_employee(self):
        self.EC=input("Enter your employee code")
        self.S=input("Enter your salary")
        
class manager(employee):
    def __init__(self):
        employee. __init__(self)
    def show_manager(self):
        print("Department code=",self.DC)
        print("Dept head=",self.h)
        print("Experience",self.ex,"years")
        
    def get_manager(self):
        self.DC=input("Enter your department code")
        self.h=input("Enter your department head name")
        self.ex=input("Enter your experience in years")
m=manager()
m.get_person()
m.get_employee()
m.get_manager()
print('*'*25)
m.show_person()
m.show_employee()
m.show_manager()


