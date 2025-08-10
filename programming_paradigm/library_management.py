class Book:
    def __init__ (self, title, author):
        self._is_checked_out = False
        self.title = title
        self.author = author
    def __str__(self):
        return f"{self.title} by {self.author}"
    def checkout(self):
        self._is_checked_out = True
    def return_book(self):
        self._is_checked_out = False

class Library:
    def __init__(self):
        self._books = []
        self.in_lib_books = []
    def add_book(self, book):
        self._books.append(book)
        self.in_lib_books.append(book)
    def check_out_book(self, title):
        for book in self.in_lib_books:
            if book.title == title and book._is_checked_out == False:
                self.in_lib_books.remove(book)
                book.checkout()
    def return_book(self, title):
        for book in self._books:
            if book.title == title and book._is_checked_out == True:
                self.in_lib_books.append(book)
                book.return_book()
    def list_available_books(self):
        for book in self.in_lib_books:
            print(book)