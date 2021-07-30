# TODO: Create a local password manager.
from tkinter import *
from tkinter import messagebox

# Constants:
FONT = ("San Francisco", 10, "bold")
YELLOW = "#FDCA40"
PURPlE = "#542E71"
PURPLE_TWO = "#A799B7"
USERNAME = "i.oberemok777@gmail.com"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


# ---------------------------- SAVE PASSWORD ------------------------------- #

# TODO: Save user data to data.txt file.
def save():
    # Get hold of all the data
    website = website_entry.get()
    user = username_entry.get()
    password = password_entry.get()

    # Check if user filled all entries
    if len(password) != 0 and len(website) != 0:

        # Message box:
        is_ok = messagebox.askokcancel(title=messagebox, message=f"These are the details entered: \nEmail: {user} "
                                                                 f"\nPassword: {password} \nSave information?")
        if is_ok:
            # Data.txt
            with open("data.txt", "a") as data_file:
                data_file.write(f"\nWEBSITE: {website} | USERNAME: {user} | PASSWORD: {password}")

            # Clear the file if user wants to:
            with open("data.txt", "r+") as data_file:
                if password == "Clear" and website == "Clear":
                    data_file.truncate(0)

            # Clear the entries
            website_entry.delete(0, END)
            password_entry.delete(0, END)

            # Return cursor to the website entry
            website_entry.focus()
    else:
        messagebox.showerror(title="Something Not Right", message="PLease do not any fields empty!")


# ---------------------------- UI SETUP ------------------------------- #
# Setup the window:
window = Tk()
window.title("Password Manager")
window.config(padx=100, pady=100, bg=YELLOW)


# TODO: 1. Create a canvas and an image in this canvas.
canvas = Canvas(width=200, height=200, highlightthickness=0, bg=YELLOW)
logo_image = PhotoImage(file="logo.png")
image_on_canvas = canvas.create_image(100, 100, image=logo_image)
canvas.grid(column=1, row=0, padx=20, pady=20)

# TODO: 2. Create labels, buttons and entries.

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
website_entry.grid(column=1, row=1, columnspan=2, sticky=EW, pady=10, padx=10)
website_entry.focus()

username_entry = Entry(fg=PURPlE, font=FONT)
username_entry.grid(column=1, row=2, columnspan=2, sticky=EW, pady=10, padx=10)
username_entry.insert(0, USERNAME)

password_entry = Entry(fg=PURPlE, font=FONT)
password_entry.grid(column=1, row=3, sticky=EW, pady=10, padx=10)

# Buttons:
generate_password = Button(text="Generate Password", font=FONT, fg=PURPlE, bg=PURPLE_TWO)
generate_password.grid(column=2, row=3, sticky=EW, pady=10, padx=10)

add_button = Button(text="Add", font=FONT, fg=PURPlE, bg=PURPLE_TWO, width=35, command=save)
add_button.grid(column=1, row=4, columnspan=2, sticky=EW, pady=10, padx=10)

# The end
window.mainloop()
