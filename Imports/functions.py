# Imports
from Imports.classes import Book
from Imports.easystring import get_string_matches

# Append a value to a tuple
def append_to_tuple(t: tuple, value) -> None:
    t = t + (value,)

# Create Book from tuple attributes
def create_book(attributes: tuple):
    return Book(*attributes)

# Save a tuple of books to the provided file
def save_books_to_file(books: tuple[Book], filename: str):
    print(str(books[0].dump()))
    with open(filename, "w") as file:
        for i in books:
            file.write(str(i.dump()).replace('"', '')+"\n")

#def reformat_to_list(s):
#    return "a"

# Format a Book() tuple
def format_book_tuple(t: tuple):
    return_tuple = ()
    for i in t:
        print(i)

# Decoding
def load_books_from_file(filename: str):
    with open(filename, 'r') as file:
        load = file.readlines()
        
    return tuple(load)

# Repeat a string the specified amount of times
def repeat_string(s: str, repeats: int):
    return_string = ""
    
    for i in range(repeats):
        return_string + s

    return return_string

# Covert a boolean to "Yes" or "No"
def bool_to_yes_no(boolean: bool):
    if boolean:
        return "Yes"
    else:
        return "No"

# Search for books in a tuple of books
def search(search: str, books: tuple[Book]):
    result = {}
    print(books)
    for i in books:
        print("data", i)
        matches = round(get_string_matches(i.info_title(), search) * 2)
        matches += get_string_matches(i.info_author(), search)
        matches += round(get_string_matches(i.info_genre(), search) / 4)
        matches += round(get_string_matches(i.info_type(), search) / 10)

        result[i] = matches

    return dict(sorted(result.items(), key=lambda item: item[1], reverse=True))