#Program to check Armstrong number
a=int(input("Enter a number"))
c=0
b=a
while b>0:
    r=b%10
    c=c+r**3
    b=b//10
if c==a:
    print("It is an armstrong number")
else:
    print("It is not an armstrong number")
