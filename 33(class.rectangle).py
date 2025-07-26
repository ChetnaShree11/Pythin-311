#Create a class rectangle contaning functions area and perimeter
class rectangle:
    def __init__(self,l,b):
        self.x=l
        self.y=b
    def area(self):
        return self.x*self.y
    def perimeter(self):
        return 2*(self.x+self.y)
L=int(input("Length of rectangle="))
B=int(input("Breadth of rectangle="))
R1=rectangle(L,B)
print("Area of rectangle=",R1.area())
print("Preimeter of rectangle=",R1.perimeter())
