import pickle
file1=open('File1.txt','rb')
data=pickle.load(file1)
print("Showing the pickled data:")
print(data)
cnt=0
for keys in data:
    print("The data",cnt,"is:",data[keys])
    cnt+=1
file1.close()







