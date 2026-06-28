class Book:
    def __init__(self,title):
        self.title=title
        self.is_available=True

class Library:
    def __init__(self):
        self.books=[]

    def add_book(self,book):
        self.books.append(book)

    def borrow_book(self,title):
        for book in self.books:
            if book.title==title and book.is_available:
                book.is_available=False
                return f"You borrowed '{title}' "
            return "Book not available"
        
lib=Library()
lib.add_book(Book("Harry Potter"))
lib.add_book(Book("The Twilight Saga"))
#print(lib.borrow_book("Harry Potter"))

