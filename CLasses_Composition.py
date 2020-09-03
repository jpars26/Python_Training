#Quando usar composição?
#É quando voce tem um classe que contem um monte de outras classes ou uma classe que tem um tanto delas

#Herança diz que um livro é uma estante de livros. Compisiçao significa que uma estande tem muitos livros 


class BookShelf:
    def __init__(self, *books):
        self.books = books
    
    def __str__(self):
        return f"BookShelf with {len(self.books)} books"

class Book:
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return f"Book {self.name}"


book = Book("Harry Potter")
book2 = Book("Piratas do Caribe")
shelf = BookShelf(book, book2)

print(shelf)