from iterator_interface import Iterator

class BookIterator(Iterator):
    def __init__(self, books):
        self.books = books
        self.index = 0

    def has_next(self):
        return self.index < len(self.books)
    
    def next(self):
        book = self.books[self.index]
        self.index += 1
        return book
