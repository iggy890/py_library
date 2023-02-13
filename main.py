# Imports
print("Importing")
from Imports.easystring import get_string_matches
from Imports.classes import *
from Imports.functions import *
from tkinter import Tk, Entry, Label, Button

VERSION = 0.1
NUM_SPACES = 35

# Create books
harry_potter = Book("Harry Potter and the Philosopher's Stone", "J.K Rowling", Genre.Fantasy, Type.Fiction)
yes = Book("Waste of Space", "Stuart Gibbs", Genre.Fantasy, Type.Fiction)
book_one = Book("Charlie Thorne 1", "Stuart Gibbs", Genre.Fantasy, Type.Fiction)
book_2 = Book("Charlie Thorne 2", "Stuart Gibbs", Genre.Fantasy, Type.Fiction)
book_3 = Book("Charlie Thorne 3", "Stuart Gibbs", Genre.Fantasy, Type.Fiction)

books = (harry_potter, yes, book_one, book_2, book_3)

print("Creating window...")

# Initiate the Tk window
window = Tk()
window.title(f"Library Manager {VERSION}")
window.geometry("800x800")

# Create the search bar
search_box = Entry(window, width=80)
search_box.grid(column=0, row=0)

s = Bar(window, 80)
t = s.return_text()

# Create the results
results_label = Label(window, text=f"Welcome to py_library {VERSION}")
results_label.grid(column=0, row=1)

def clicked():
    txt = search_box.get()
    results = search(txt, books)
    s.clear()

    for i, j in zip(results.keys(), results.values()):
        display_info = i.dump()
        print(NUM_SPACES - len(display_info))
        s.add_button(Button(t, text="{}\n".format(display_info, *repeat_string(" ", NUM_SPACES - len(display_info)))))


# Create the search button
search_button = Button(window, text="Search", command=clicked)
search_button.grid(column=1, row=0)

search("i", books)
save_books_to_file(books, "saves.txt")

# Run the window
window.mainloop()