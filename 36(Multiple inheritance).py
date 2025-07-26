#Multiple inheritance
class A():
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def sum(self):
        c=self.a+self.b
        return c
    def sub(self):
        c=self.a-self.b
        return c

class B():
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def prod(self):
        c=self.a*self.b
        return c
    def div(self):
        c=self.a/self.b

class C(A,B):
    def __init__(self,a,b):
        A.__init__(self,a,b)
        B.__init__(self,a,b)
    def av(self):
        c=(self.a+self.b)/2
        return c

x=int(input("Enter a number"))
y=int(input("Enter another number"))
m=C(x,y)
print("Sum=",m.sum())
print("Average=",m.av())
