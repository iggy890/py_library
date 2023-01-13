from classes import Book, Result

# Append a value to a tuple
def append_to_tuple(t: tuple, value) -> None:
    t = t + (value,)

# Save a tuple of books to the provided file
def save_books_to_file(books: tuple[Book], filename: str):
    with open(filename, 'w') as file:
        file.write(list(books))

# TODO Finish this
def load_books_from_file(filename: str):
    with open(filename, 'r') as file:
        load = file.read()

    print(list(load))

# Search for books in a tuple of books
def search(search: str, books: tuple[Book]):
    return list(Result(search, books))