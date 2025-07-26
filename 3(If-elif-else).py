#Find the average marks in 4 subjects out of 100
Sub1=int(input("Marks obtained in english="))
Sub2=int(input("Marks obtained in maths"))
Sub3=int(input("Marks obtained in science"))
Sub4=int(input("Marks obtained in hindi="))
Average=(Sub1+Sub2+Sub3+Sub4)/4
print("Average marks=",Average)
if Average<50:
    print("Fail")
else:
    print("pass")
print("Thank you")


print('\n')


"""Find net pay of an employ on the basis of his basic pay,
where net pay=basic pay+HRA+DA and HRA=20% of basic pay"""

Basic_pay=int(input("Basic pay="))
if Basic_pay>=50000:
    HRA=(20/100)*Basic_pay
    DA=(30/100)*Basic_pay
else:
    HRA=(15/100)*Basic_pay
    DA=(20/100)*Basic_pay
Net_pay=Basic_pay+HRA+DA
print("HRA=",HRA)
print("DA=",DA)
print("Net pay=",Net_pay)


print('\n')


#To find if a number is even or odd
a=int(input("Enter a number"))
if a%2==0:
    print("It is even")
else:print("It is odd")


print('\n')


#To find sum,product or difference of two numbers
a=int(input("Enter a number"))
b=int(input("Enter another number"))
c=input("Operation{Add\Subtarct\Multiply}=")
if c=="Add":
    Result=a+b
elif c=="Subtract":
    Result=a-b
elif c=="Multiply":
    Result=a*b
else:
    Result=0
    print("Invalid Symbol")
print("Result=",Result)


print('\n')


#Grading of student scores
a=int(input("Marks in english="))
b=int(input("Marks in hindi="))
c=int(input("Marks in maths="))
d=int(input("Marks in science="))
p=(a+b+c+d)/4
print("Percentage=",p)
if p>90:
    print("A")
elif p>80:
    print("B")
elif p>70:
    print("C")
elif p>60:
    print("D")
else:
    print("Fail")
    print("Better luck next time")


print('\n')


#Calculate commision of a sales men on the basis if his sales amount
SA=int(input("Enter the Sales Amount"))
if SA>=100000:
    C=(25/100)*SA
elif SA>=50000:
    C=(15/100)*SA
elif SA>=25000:
    C=(10/100)*SA
else:
    C=0
print("Commission=",C)


print('\n')


#Find the largest of two numbers
a=int(input("Enter first number"))
b=int(input("Enter second number"))
if a>b:
      print(a,"is greater than",b)
else:
    print(b,"is greater than",a)


print('\n')


#Find the largest of three numbers
a=int(input("Enter first number"))
b=int(input("Enter second number"))
c=int(input("Enter third number"))
if a>b:
      if a>c:
            print(a,"is the largest")
elif b>a and b>c:
            print(b,"is the largest")
elif c>a and c>b:
            print(c,"is the largest")
else:
      print("All are equal")


print('\n')


#Find whether the given candidate is eligible to vote
Age=int(input("Enter your age"))
if Age>=18:
    print("Eligible")
else:
    print("Not eligible")





