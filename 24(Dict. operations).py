#Merge two python dictionaries.
d1={1:'a',2:'b',3:'c',4:'d',5:'e'}
d2={6:'f',7:'g',8:'h'}
d1.update(d2)
print(d1)



print("Next")



#Create a dictionary with student's name and marks in history and maths and display the value of history marks.
d1={'chetna':(90,80),'prerna':(95,81),'rekha':(70,40),'varsha':(60,30)}
for h in d1:
    print(d1[h][0])




print("Next")




#Create a dictionary with name, age, sallary and city of employee. Hence, remove name and sallary from the dictionary.
D={'E1':['Sangeeta',21,30000,'Jammu'],'E2':['Revati',30,40000,'Kashmir'],'E3':['Ajay',35,60000,'Poonch'],'E4':['Naina',18,100000,'Delhi']}
for i in D:
    del D[i][0]
    del D[i][1]
print(D)


print('NEXT')




#Create a dictionary with employee name and his designation and create a list of employees whose designation in manager.
En={'Mehata':'CEO','Tata':'Manager','Birla':'Sweeeper','Ambani':'Manager','Singhania':'Junior','Khan':'Manager','Armaan':'Guard'}
l=[]
for a,b in En.items():
    if b=='Manager':
        l.append(a)
print(l)



print('NEXT')



#Write a program to create two dictionary objects named states and cities with the following items
States={'Oregon':'OR','Florida':'FL','California':'CA','New York':'NY','Michigan':'MI'}
Cities={'CA':'San Francisco','MI':'Detroit','FL':'Jacksinville'}
a={'NY':'NewYork','OR':'Portland'}
Cities.update(a)
print(Cities.items())







       

