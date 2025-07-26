#Find average of 3 numbers using def function
def average(a,b,c):
    av=(a+b+c)/3
    return av
x=int(input("First number="))
y=int(input("Second number="))
z=int(input("Third number="))
print("Average of these numbers=",average(x,y,z))


print("NEXT")


#Find SI
def Simple_interest(P,R,T):
    SI=(P*R*T)/100
    return SI
a=int(input("Principle="))
b=int(input("Rate of interest="))
c=int(input("Time period="))
print("Simple Interest=",Simple_interest(a,b,c))


print("NEXT")


#Find if a number is odd or even
def odd_even(n):
    if n%2==0:
        return "Even"
    else:
        return "odd"
a=int(input("Enter a number"))
print(odd_even(a))



print("NEXT")



#Convert temperature given in C to F
def temp(t):
    F=(t*(9.0/5))+32.0
    return F
C=int(input("Enter the temperature in degree celsius"))
print("Temperature in fahrenheit=",temp(C))



print("NEXT")



#Count digits in a number
def count_digits(n):
    n=0
    for x in a:
        n=n+1
    return n
a=input("Enter a number")
print("Number od digits in the number=",count_digits(a))



print("NEXT")



#Herons formulla
def herons_formulla(a,b,c):
    s=(a+b+c)/2
    A=(s*(s-a)*(s-b)*(s-c))**(0.5)
    return A
x=float(input("Side 1="))
y=float(input("Side 2="))
z=float(input("Side 3="))
print("Area of the triangle=",herons_formulla(x,y,z))

    
    
    






