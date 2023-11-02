import tkinter
from tkinter import END
from tkinter import messagebox
import random
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
               'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
               'p',
               'q', 'r', 's', 't',
               'u', 'v', 'w', 'x', 'y', 'z']

    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '@', '#', '$', '%', '^', '&', '*']

    letters_count = random.randint(8, 10)
    numbers_count = random.randint(2, 4)
    symbols_count = random.randint(2, 4)

    # password = []
    password = [random.choice(letters) for i in range(letters_count)]

    password += [random.choice(numbers) for i in range(numbers_count)]

    password += [random.choice(symbols) for i in range(symbols_count)]

    random.shuffle(password)
    password = ''.join(password)
    password_entry.insert(0, password)
    # copying the password to clipboard
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {website: {
        "email": email,
        "password": password
    }}

    if len(website) == 0 or len(password) == 0 or len(email) == 0:
        messagebox.askokcancel(title="OOPS", message="Don't leave any fields empty")

    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the entered details:\nEmail: {email}\n"
                                                              f"Password: {password}")
        if is_ok:
            try:
                with open("credentials.json", "r") as cred_file:
                    # Reading the data from the file
                    data = json.load(cred_file)
            except FileNotFoundError:
                # inserting the first record when the file not exist
                with open("credentials.json", "w") as cred_write_file:
                    json.dump(new_data, cred_write_file, indent=4)
            else:
                # when already the data present inside the json file, we will update that data_dict with the new_data
                # and will write to the json file
                data.update(new_data)
                with open("credentials.json", "w") as cred_write_file:
                    # writing the data to the file
                    json.dump(data, cred_write_file, indent=4)
            finally:
                website_entry.delete(0, END)
                # email_entry.delete(0, END)
                password_entry.delete(0, END)


# ----------------------------------FIND_PASSWORD------------------------------------------


def find_password():
    website = website_entry.get()
    try:
        with open("credentials.json", 'r') as cred_file:
            data = json.load(cred_file)
    except FileNotFoundError:
        messagebox.askokcancel(title="OOPS", message="No credentials file found")
    else:
        if website in data:
            messagebox.showinfo(title="Website", message=f"website: {website}\nEmail: {data[website]['email']}\n "
                                                         f"Password: {data[website]['password']}")
        else:
            messagebox.askokcancel(title="Not Found", message=f"No details for the {website} exists")


# ---------------------------- UI SETUP ------------------------------- #

window = tkinter.Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = tkinter.Canvas(width=160, height=180)
logo_img = tkinter.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Labels
website_label = tkinter.Label(text="Website:")
website_label.grid(row=1, column=0)

email_label = tkinter.Label(text="Email/Username:")
email_label.grid(row=2, column=0)

password_label = tkinter.Label(text="Password:")
password_label.grid(row=3, column=0)

# Entries
website_entry = tkinter.Entry(width=27, highlightthickness=1)
website_entry.focus()
website_entry.grid(row=1, column=1)

email_entry = tkinter.Entry(width=45, highlightthickness=1)
# Populating/displaying something before any value entered
email_entry.insert(0, "xyz@email.com")
email_entry.grid(row=2, column=1, columnspan=2)

password_entry = tkinter.Entry(width=27, highlightthickness=1)
password_entry.grid(row=3, column=1, sticky='N')

# Buttons
search_button = tkinter.Button(text="Search", width=14, bg="#0000ff", command=find_password)
search_button.grid(row=1, column=2)

generate_pass_button = tkinter.Button(text="Generate Password", command=generate_password)
generate_pass_button.grid(row=3, column=2)

add_button = tkinter.Button(text="Add", width=39, highlightthickness=1, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
