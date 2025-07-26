#To check whether the given year is leap or not
a= int(input("Enter the year"))
if a%4==0:
    if a%100!=0:
        print("It is a leap year")
    elif a%100==0:
         if a%400==0:
            print("It is a leap year")
         elif a%400!=0:
            print("It is not a leap year")
            
else:
    print("It is not a leap year")
            
            
            
        
