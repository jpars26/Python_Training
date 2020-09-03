class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# __str__ é quando vc quer tranformar um objeto em uma string
    def __str__(self):
        return f"{self.name} have {self.age} years old"


#__repr__ é usado para imprimir uma representação nao abigua de um objeto, para que voce possa usa-lo para recriar o objeto
    def __repr__(self):
        return f"<Person ('{self.name}' {self.age})>"

bob = Person("Bob", 25)
print(bob)