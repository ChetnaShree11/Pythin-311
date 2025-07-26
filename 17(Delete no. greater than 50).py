#Create a list of integers then remove the items from the list wherever the number is greater than 50.
a=[2,4,50,6,55,23,45,64,33,45,80]
for i in a:
    if i>50:
        a.remove(i)
print(a)
