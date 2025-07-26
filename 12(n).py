#To find the sum of following series:1,11,111,1111
n=1
sum=0
while(n<=1111):
    print(n,end="+")
    sum=sum+n
    n=n*10+1
print("\b\nSum=",sum)




#To find the sum of following series:1,11,111,1111,11111.....upto n terms
a=int(input("Enter the number of terms"))
sum=0
n=1
for t in range(1,a+1):
    print(n,end="+")
    sum=sum+n
    n=n*10+1
print("\b\nSum=",sum)
    



