from Imports.easystring import get_string_matches
from Imports.classes import *
from Imports.functions import *
from tkinter import Tk, Entry, Label, Button

window = Tk()
window.title("Library Manager")
window.geometry("800x800")

search_box = Entry(window, width=30)
search_box.grid(column=1, row=0)

search_button = Button(window, text="Search")
search_button.grid(column=2, row=0)

harry_potter = Book("Harry Potter and the Philosopher's Stone", "J.K Rowling", Genre.Fantasy)
yes = Book("Waste of Space", "Stuart Gibbs", Genre.Fantasy, Type.Fiction)

books = (harry_potter, yes)

save_books_to_file(append_to_tuple(books, yes), "saves.txt")

Result("i", books)

window.mainloop()