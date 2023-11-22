#Demonstrate the use of built-in functions

#The abs() function returns the absolute value of a number
print(abs(-10))

#The len() function returns the length of a string or a sequence
print(len("Welcome to, MIET|"))

#The min() function returns the minimum value of a sequence
print(min([10, 20, 30]))

#The round() function rounds a number to to a specified number of decimal places
print(round(3.14159,2))

#The isalnum() function returns True if the string contains only alphanumeric characters, False otherwise
print("CSE,3rd sem!".isalnum())
print("123abc".isalnum())

#The type() function returns the type of an object
print(type(10))
print(type("AI and, ML!"))




#Extras: 

#all() - Returns true if all elements in an iterable are true, false otherwise
l1=[True, True, True]
l2=[True, False, True]
print(all(l1))
print(all(l2))

#any() - Returns true if any element in an iterable is true, false otherwise
l3=[False, False, False]
l4=[True, False, False]

#ascii() - Returns a string containing a printable representation of an object
#It is used to get a printable representation of an object, not its ASCII value
print(ascii("Kot, \nBhalwal!"))

#The ord() function returns the unicode print of a character, which is a more comprehensive character encoding than ASCII
print(ord("a"))
print(ord(" "))
print(ord(","))
print(ord("*"))

#bin() - Converts an integer to a binary string
print(bin(10))
print(bin(15))

#bool() - Converts  a value to Boolean
print(bool(0))
print(bool(42))
print(bool([]))
print(bool([1,2]))

#bytearray() - Returns a mutable bytearray object from an iterable of integers
BA=bytearray([65,66,67])
print(BA)
BA[0]=88 #ASCII value for x
print(BA)

#bytes() - Returns an immutable bytes object from an iterable of integers
BS=bytes([68,69,70])
print(BS)

#callable() - Returns true if the object appears callable(can be called as a function), false otherwise
def func():
    return 42
print(callable(func))
print(callable(42))


                  


