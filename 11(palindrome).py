#Check if the given number is a palindrome or not
a=input("Enter a number")
b=a[::-1]
if a==b:
      print("It is a palindrome")
else:
    print("It is not a palindrome")



a=int(input("Enter a number"))
num=a
b=0
while (a>0):
    a,r=divmod(a,10)
    b=b*10+r
print(b)
if (num==b):
    print("It is a palindrome")
else:
    print("It is not a palindrome")


