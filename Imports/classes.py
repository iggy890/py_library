from tkinter import Scrollbar, Button, Text

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
        self.on_loan = is_being_borrowed

    def display_info(self) -> str:
       return f"{self.title} by {self.author}" 

    def return_loan_state(self) -> bool:
        return self.on_loan

    def borrow(self) -> None:
        self.on_loan = True
    
    def return_book(self) -> None:
        self.on_loan = False

    def dump(self) -> tuple:
        return (self.title, self.author, self.genre, self.type, self.is_being_borrowed)

    def create_book(self, attributes: tuple):
        return Book(*attributes)

class Bar:
    def __init__(self, window):
        text = Text(window)
        text.grid(column=0, row=2)
        self.text = text

        sb = Scrollbar(window, command=text.yview)
        sb.grid(column=0, row=1)
        self.sb = sb


    def return_text(self) -> Text:
        return self.text

    def add_button(self, button: Button):
        self.text.configure(state="normal")

        self.text.configure(yscrollcommand=self.sb.set)
        self.text.window_create("end", window=button)
        self.text.insert("end", "\n")

        self.text.configure(state="disabled")
    


# Create the classes
Type = type()
Genre = genre()