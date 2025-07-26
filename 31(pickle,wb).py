import pickle
file1=open("File1.txt",'wb')
Student={}
R=int(input("Enter Roll no. of student"))
N=input("Enter name")
M=float(input("Enter marks"))
Student['Roll_No']=R
Student['Name']=N
Student['Marks']=M
pickle.dump(Student,file1)
file1.close()
