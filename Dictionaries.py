friend_ages = {"Joao": 24, "Marco": 25, "Jose": 30}

 #Adicionar ou alterar um valor no dicionario

friend_ages["Bob"] = 20
friend_ages["Joao"] = 30

print(friend_ages)

#Um dicionario com varias coisas é normal ter uma lista de dicionarios
friends = [
     {"name": "Joao", "age": 24},
     {"name": "Maria", "age": 30},
     {"name": "Jose", "age": 40},
     ]

print(friends[1]["age"])
s
#Desestruturação

student_attendance = {"Joao": 24, "Marco": 25, "Jose": 30}

for student, attendend in student_attendance.items():
     print(f"{student}: {attendend}")

#Desestruturar uma lista formando outras *tail

haed, *tail = [1,2,3,1,5,6]    
print(haed)
print(tail)