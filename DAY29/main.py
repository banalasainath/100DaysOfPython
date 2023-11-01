import tkinter
from tkinter import END
from tkinter import messagebox
import random
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
               'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
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

    if len(website) == 0 or len(password) == 0 or len(email) == 0:
        messagebox.askokcancel(title="OOPS", message="Don't leave any fields empty")

    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the entered details:\nEmail: {email}\n"
                                                              f"Password: {password}")
        if is_ok:
            with open("credentials.txt", "a") as cred_file:
                cred_file.write(f"{website} | {email} | {password}\n")
                website_entry.delete(0, END)
                # email_entry.delete(0, END)
                password_entry.delete(0, END)


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
website_entry = tkinter.Entry(width=45)
website_entry.focus()
website_entry.grid(row=1, column=1, columnspan=2)

email_entry = tkinter.Entry(width=45)
# Populating/displaying something before any value entered
email_entry.insert(0, "xyz@email.com")
email_entry.grid(row=2, column=1, columnspan=2)

password_entry = tkinter.Entry(width=27)
password_entry.grid(row=3, column=1, sticky='N')

# Buttons
generate_pass_button = tkinter.Button(text="Generate Password", command=generate_password)
generate_pass_button.grid(row=3, column=2)

add_button = tkinter.Button(text="Add", width=37, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
