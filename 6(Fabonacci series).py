#Display the Fibonacci series up to a maximum limit
n=int(input("Enter the maximum number"))
a=0
b=1
c=a+b
print(c,end=',')
for x in range(1,n):
    print(c,end=',')
    a=b
    b=c
    c=a+b
    




    
