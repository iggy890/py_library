# Imports
print("Importing")
from Imports.easystring import get_string_matches
from Imports.classes import *
from Imports.functions import *
from tkinter import Tk, Entry, Label, Button

VERSION = 0.1

# Create books
harry_potter = Book("Harry Potter and the Philosopher's Stone", "J.K Rowling", Genre.Fantasy, Type.Fiction)
yes = Book("Waste of Space", "Stuart Gibbs", Genre.Fantasy, Type.Fiction)

books = (harry_potter, yes)


print("Creating window...")
# Initiate the Tk window
window = Tk()
window.title(f"Library Manager {VERSION}")
window.geometry("800x800")

# Create the search bar
search_box = Entry(window, width=30)
search_box.grid(column=0, row=0)

# Create the results
results_label = Label(window, text=f"Welcome to py_library {VERSION}")
results_label.grid(column=0, row=1)

def clicked():
    txt = search_box.get()
    results = search(txt, books)
    string = ""
    print(results)

    for i, j in zip(results.keys(), results.values()):
        string += f"{i.display_info()}: {j}\n"

    results_label.configure(text=string)


# Create the search button
search_button = Button(window, text="Search", command=clicked)
search_button.grid(column=2, row=0)

search("i", books)
save_books_to_file(books, "saves.txt")

# Run the window
window.mainloop()