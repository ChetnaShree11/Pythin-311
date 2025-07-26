#Input numbers and display the smallest and largest number
n=int(input("How many numbers"))
list1=[]
for i in range(1,n+1):
    a=int(input("Enter the number"))
    list1.append(a)

print("Largest number=",max(list1))
print("Smallest number=",min(list1))


print("NEXT")    

#Generate the even numbers upto a giver number
x=int(input("Enter a number"))
a=1
while a<x:
    if a%2==0:
        print(a,end=',')
    a=a+1

