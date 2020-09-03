# Uma função dentro de uma class é chamada de metodo
#Self é sempre obrigatorio, depois pode colocar parametros (cria um objeto vazio para armazenar informaçoes)
# __init__ são chamados de metodos especiais, mas são metodos tbm
class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def media(self):

        return sum(self.grades)/ len(self.grades)

student = Student("Bob", (90, 50, 30, 90, 100))
student2 = Student("Joao", (90, 50, 80, 90, 100))
print(student.name)
print(student.media())

print(student2.name)
print(student2.media())