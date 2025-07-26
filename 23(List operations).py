#Make string from an input string with words in reverse order.
a=input("Enter a string")
b=a.split()
b.reverse()
print(b)
d=''.join(b)
print(d)



print("NEXT")



'''Get a list of words with their count in a sentence.The words should be in sorted
order alphabetically.Words should not be repeated.Assume space as a seperator for words.'''
a=[]
ch="y"
while ch=="y":
    w=input("Enter the word")
    if w in a:
        print("Word already exists")
        continue
    else:
        c=input("Enter the count")
        w=w,c
        a.append(w)
        
    ch=input("Enter y to continue, any other letter to exit")
a.sort()
print(a)
    
    






