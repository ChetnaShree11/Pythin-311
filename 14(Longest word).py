#Input a sentence and display the longest word
a=input("Enter a sentence")
i=a.split(" ")
b=list(i)
print(max(b,key=len))
