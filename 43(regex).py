#Write a functoion that would validate the following enrollment
def valid():
    import re
    p=re.compile("U1011\d\dF(CS|EC|BT)\d\d\d")
    eno=input("Enter the pattern")
    if (p.match(eno)):
        print('This enrollment number is valid')
    else:
         print('This enrollment number is invalid')

valid()
