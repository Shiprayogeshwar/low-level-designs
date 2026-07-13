
from book_iterator import BookIterator


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def create_iterator(self):
        return BookIterator(self.books)
