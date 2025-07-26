#Find whether a user has earned profit or loss using SP and CP
CP=int(input("Enter the cost prize"))
SP=int(input("Enter the selling prize"))
if CP>SP:
    print("Loss")
elif SP>CP:
    print("Profit")
else:
    print("Neither profit nor loss")
