from Imports.easystring import get_string_matches

# Genre class for book genres
class genre:
    def __init__(self) -> None:
        self.Adventure = "Adventure"
        self.Classics = "Classics"
        self.Crime = "Crime"

        self.Fairy_Tale = "Fairy Tale"
        self.Fables = "Fables"
        self.Folk_Tales = "Folk Tales"
        self.Fantasy = "Fantasy"

        self.Historical_Fiction = "Historical Fiction"
        self.Horror = "Horror"
        self.Humuor = "Humuor"

        self.Satire = "Satire"

# Type class for Fiction or Non-Fiction
class type:
    def __init__(self):
        self.Fiction = "Fiction"
        self.Non_Fiction = "Non-Fiction"

# Book class, containing the title, author and genre
class Book:
    def __init__(self, title: str, author: str, genre: str, type: str, is_being_borrowed: bool = False) -> None:
        self.title = title
        self.author = author
        self.genre = genre
        self.type = type
        self.is_being_borrowed = is_being_borrowed

    def display_info(self) -> str:
       return f"{self.title} by {self.author}" 

    def borrow(self) -> None:
        self.is_being_borrowed = True
    
    def return_book(self) -> None:
        self.is_being_borrowed = False

    def dump(self) -> tuple:
        return (self.title, self.author, self.genre, self.type, self.is_being_borrowed)

    def create_book(self, attributes: tuple):
        return Book(*attributes)


# Create the classes
Type = type()
Genre = genre()