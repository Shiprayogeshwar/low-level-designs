from library import Library



if __name__ == "__main__":
    library = Library()
    library.add_book("James Bond")
    library.add_book("Harry Potter")
    library.add_book("Atomic Habits")

    iterator = library.create_iterator()

    while iterator.has_next():
        print(iterator.next())