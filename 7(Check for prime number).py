#To find if a number is prime
a=int(input("Enter a number"))
flag=0
for x in range(2,(a//2)+1):
               if a%x==0:
                   flag=1
                   break 
if flag==1:
    print("It is not a Prime number")
else:
    print("It is a prime number")

