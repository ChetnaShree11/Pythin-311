#Find the factorial of a number n
n=int(input("Enter the number"))
product=1
c=1
while c<=n:
    product=product*c
    c=c+1
print("Factorial=",product)




n=int(input("Enter the number"))
f=1
for x in range(1,n+1):
    f=f*x
print("factorial=",f)
    
    
