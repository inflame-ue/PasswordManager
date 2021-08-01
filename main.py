from tkinter import *
from tkinter import messagebox
from random import shuffle, randint, choice
import pyperclip
import json
# Constants:
FONT = ("San Francisco", 10, "bold")
YELLOW = "#FDCA40"
PURPlE = "#542E71"
PURPLE_TWO = "#A799B7"
RED = "#FB3640"
USERNAME = "inflame"  # ADD YOUR USERNAME HERE


# Password generation
def generate_password():
    """Generates a password if 'generate password' button was pressed."""
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(10, 20))]
    password_symbols = [choice(symbols) for _ in range(randint(5, 10))]
    password_numbers = [choice(numbers) for _ in range(randint(5, 10))]

    password_list = [*password_letters, *password_symbols, *password_numbers]
    shuffle(password_list)

    password = "".join(password_list)

    password_entry.insert(0, password)
    pyperclip.copy(password)


def save():
    """Saves information the .json file if 'add' button was pressed."""
    # Get hold of all the data
    website = website_entry.get()
    user = username_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "user": user,
            "password": password
        }
    }

    # Check if user filled all entries
    if len(password) != 0 and len(website) != 0:
        # Open or create the file.
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        except (FileNotFoundError, json.JSONDecodeError):
            data = new_data
        else:
            data.update(new_data)

        with open("data.json", "w") as data_file:
            json.dump(data, data_file, indent=4)

        # Clear the entries
        website_entry.delete(0, END)
        password_entry.delete(0, END)

        # Return cursor to the website entry
        website_entry.focus()
    else:
        messagebox.showerror(title="Something Not Right", message="PLease do not any fields empty!")


def clear():
    """Clears the .json file if '!clear data!' button was pressed."""
    want_to_clear = messagebox.askokcancel(title="Clear Information", message="Are you sure you want to clear all the "
                                                                              "data from data.txt?")
    if want_to_clear:
        # Clear the data.txt
        with open("data.json", "r+") as file:
            file.truncate(0)


def search():
    """
    If search button was pressed: searching through the .json file.
    Returns messagebox with information if it exists.
    Returns error messagebox if information or file does not exist.
    """
    website_to_search = website_entry.get()

    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except json.JSONDecodeError:
        messagebox.showerror(title="Error", message="No Data File Found.")
    else:
        if website_to_search in data:
            messagebox.showinfo(title=data[website_to_search], message=f"Username: {data[website_to_search]['user']}"
                                                                       f"\nPassword: "f"{data[website_to_search]['password']} ")
        else:
            messagebox.showerror(title="No website", message=f"There is no such website as {website_to_search} "
                                                             f"in the data.")


# UI SETUP
# Setup the window:
window = Tk()
window.title("Password Manager")
window.config(padx=100, pady=100, bg=YELLOW)

canvas = Canvas(width=200, height=200, highlightthickness=0, bg=YELLOW)
logo_image = PhotoImage(file="logo.png")
image_on_canvas = canvas.create_image(100, 100, image=logo_image)
canvas.grid(column=1, row=0, padx=20, pady=20)

# Labels
website_label = Label(text="Website:", font=FONT, bg=YELLOW, fg=PURPlE)
website_label.config(padx=10, pady=10)
website_label.grid(column=0, row=1)

username_label = Label(text="Email/Username:", font=FONT, bg=YELLOW, fg=PURPlE)
username_label.config(padx=10, pady=10)
username_label.grid(column=0, row=2)

password_label = Label(text="Password:", font=FONT, bg=YELLOW, fg=PURPlE)
password_label.config(padx=10, pady=10)
password_label.grid(column=0, row=3)

# Entries
website_entry = Entry(fg=PURPlE, font=FONT)
website_entry.grid(column=1, row=1, sticky=EW, pady=10, padx=10)
website_entry.focus()

username_entry = Entry(fg=PURPlE, font=FONT)
username_entry.grid(column=1, row=2, columnspan=2, sticky=EW, pady=10, padx=10)
username_entry.insert(0, USERNAME)

password_entry = Entry(fg=PURPlE, font=FONT)
password_entry.grid(column=1, row=3, sticky=EW, pady=10, padx=10)

# Buttons:
generate_password_button = Button(text="Generate Password", font=FONT, fg=PURPlE, bg=PURPLE_TWO,
                                  command=generate_password)
generate_password_button.grid(column=2, row=3, sticky=EW, pady=10, padx=10)

add_button = Button(text="Add", font=FONT, fg=PURPlE, bg=PURPLE_TWO, width=35, command=save)
add_button.grid(column=1, row=4, columnspan=2, sticky=EW, pady=10, padx=10)

clear_button = Button(text="!Clear Data!", font=FONT, bg=RED, command=clear)
clear_button.grid(column=0, row=4, sticky=EW, pady=10, padx=10)

search_button = Button(text="Search", font=FONT, bg=PURPLE_TWO, fg=PURPlE, command=search)
search_button.grid(column=2, row=1, sticky=EW, padx=10, pady=10)

# The end
window.mainloop()
