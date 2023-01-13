from easystring import *

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

class type:
    def __init__(self):
        self.Fiction = "Fiction"
        self.Non_Fiction = "Non-Fiction"

# Book class, containing the title, author and genre
class Book:
    def __init__(self, title: str, author: str, genre: str, type: str) -> None:
        self.title = title
        self.author = author
        self.genre = genre
        self.type = type
        self.is_being_borrowed = False

    def display_info(self) -> str:
       return f"{self.title} by {self.author} Genre: {self.genre}" 

    def borrow(self) -> None:
        self.is_being_borrowed = True
    
    def return_book(self) -> None:
        self.is_being_borrowed = False

class Result:
    def __init__(self, search: str, books: tuple[Book]):
        result = {}

        for i in books:
            matches = round(get_string_matches(i.title, search) * 2)
            matches += get_string_matches(i.author, search)
            matches += round(get_string_matches(i.genre, search) / 4)
            matches += round(get_string_matches(i.type, search) / 10)

            result[i.title] = matches

        return dict(sorted(result.items(), key=lambda item: item[1], reverse=True))

Type = type()
Genre = genre()