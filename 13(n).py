#To generate the series: 7,77,707,7007
n=7
r=1
while(n<=7007):
    print(n,end=",")
    n=(7*(10**r))+7
    r=r+1


#To generate the series: 7,77,707,7007...upto n terms
a=int(input("Enter the number of terms"))
n=7
r=1
for t in range(1,a+1):
    print(n,end=",")
    n=(7*(10**r))+7
    r=r+1

