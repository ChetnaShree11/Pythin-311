#Count digits in a number
a=input("Enter a number")
c=0
for x in a:
    c=c+1
print("Number of digits=",c)
    


a=int(input("Enter a numbear"))
c=0
while (a>0):
    a=a//10
    c=c+1
print("Number of digits",c)


print('\n')


#Find out how many times a particular digit occurn in a numberr
a=input("Enter the number")
d=input("Enter the digit")
c=0
for x in a:
    if x==d:
        c=c+1
print("Number of digits are",c)



a=int(input("Enter the number"))
d=int(input("Enter the digit"))
c=0
while (a>0):
    r=a%10
    a=a//10
    if r==d:
        c=c+1
print("Number of digits are",c)     



