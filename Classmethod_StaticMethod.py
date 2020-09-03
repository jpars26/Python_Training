class ClassTest:
#Obtem uma instancia ou um objeto/ Se voce quer usar o objeto, ou se vc quer cirar qualquer outro tipo de instancia, nao coloca nada no topo
    def intance_method(self):
        print(f"Called instance_method of {self}")

#Se voce quer um metodo que use a classe para algo use esse metodo
    @classmethod
    def class_method(cls):
        print(f"Called class_method of {cls}")

#Esse metodo nao recebe nada quando chama ele/ Se voce quer uma função dentro da classe que nao use a classe para nada, ou instancia 
    @staticmethod
    def static_method():
        print("Called static_method")



#--------------------------------------------------------------------------------------------------------------------------

class Book:
    TYPE = ("hardcover", "paperback")

    def __init__(self, name, book_type, weight):
        self.name = name
        self.book_type = book_type
        self.weight = weight

    def __repr__(self):
        print (f"<Book {self.name}, {self.book_type}, {self.weight}>")

    @classmethod
    def hardcover(cls, name, page_weight):
        return cls(name, cls.TYPE[0], page_weight +100)
    
    @classmethod
    def paperback(cls, name, page_weight):
        return cls(name, cls.TYPE[1], page_weight)

book = Book.hardcover("Harry", 1500)
light = Book.paperback("Potter", 600)

print(book)
print(light)