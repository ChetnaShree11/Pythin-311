#Validate a URL
a=input("Enter a URL")
try:
    if (a.startswith('http://' or 'https://')):
        print("URL is valid")
    else:
        print("URL is not valid")
except:
    print("Enter a string only")
