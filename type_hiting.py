# A -> siguinifica retornar um valor ou metodo

class Book:
    TYPE = ("hardcover", "paperback")

    def __init__(self, name: str, book_type: str, weight: int):
        self.name = name
        self.book_type = book_type
        self.weight = weight

    def __repr__(self) -> str:
        print (f"<Book {self.name}, {self.book_type}, {self.weight}>")

    @classmethod
    def hardcover(cls, name: str, page_weight: int) -> "Book":
        return cls(name, cls.TYPE[0], page_weight +100)
    
    @classmethod
    def paperback(cls, name: str, page_weight: int) -> "Book":
        return cls(name, cls.TYPE[1], page_weight)