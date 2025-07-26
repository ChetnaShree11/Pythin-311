#Find the simple interest
Principle=int(input("Principle="))
Rate=int(input("Rate="))
Time=int(input("Time="))
Simple_interest=(Principle*Rate*Time)/100
print("Simple Interest=",Simple_interest)

print('\n')

#To find circumference and area of a circle
Radius=int(input("Radius="))
Circumference=2*3.14*Radius
Area=3.14*Radius**2
print("Circumference=",Circumference)
print("Area=",Area)

print('\n')

#Find the area of right angled triangle
Base=int(input("Base="))
Height=int(input("Height="))
Area=(Base*Height)/2
print("Area of Triangle=",Area)

print('\n')

#Evaluate the expression (a+b)^2
a=int(input("a="))
b=int(input("b="))
c=(a**2)+(b**2)+(2*a*b)
print("(a+b)^2=",c)

print('\n')

#Find the discriminent where d=b^2-4ac
a=int(input("a="))
b=int(input("b="))
c=int(input("c="))
d=(b**2)-(4*a*c)
print("Discriminent=",d)

