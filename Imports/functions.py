# Imports
from Imports.classes import Book
from Imports.easystring import get_string_matches

# Append a value to a tuple
def append_to_tuple(t: tuple, value) -> None:
    t = t + (value,)

# Save a tuple of books to the provided file
def save_books_to_file(books: tuple[Book], filename: str):
    with open(filename, "w") as file:
        file.write(str((i.dump() for i in books)))

# Decoding
def load_books_from_file(filename: str):
    with open(filename, 'r') as file:
        load = file.read()

    print(tuple(load))
    return tuple(load)

def bool_to_yes_no(boolean: bool):
    if boolean:
        return "Yes"
    else:
        return "No"

# Search for books in a tuple of books
def search(search: str, books: tuple[Book]):
    result = {}

    for i in books:
        matches = round(get_string_matches(i.title, search) * 2)
        matches += get_string_matches(i.author, search)
        matches += round(get_string_matches(i.genre, search) / 4)
        matches += round(get_string_matches(i.type, search) / 10)

        result[i] = matches

    return dict(sorted(result.items(), key=lambda item: item[1], reverse=True))