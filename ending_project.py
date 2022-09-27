import json
from tkinter import *
from tkinter import messagebox
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def random_password():
    letters_list = [random.choice(letters) for char in range(random.randint(8, 10))]
    symbols_list = [random.choice(symbols) for char in range(random.randint(2, 4))]
    numbers_list = [random.choice(numbers) for char in range(random.randint(2, 4))]

    password_list = letters_list + symbols_list + numbers_list
    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
    }}

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showwarning(title="Oops", message="Please don't leave any fields empty!")
    else:
        try:
            with open("data.json", "r") as data_file:
                #reading old data
                data = json.load(data_file)
        except(FileNotFoundError, json.decoder.JSONDecodeError):
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            #updating old data with new data
            data.update(new_data)

            with open("data.json", "w") as data_file:
                #saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #



window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

#logo canvas
canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

#website label
website_label = Label(text="Website:", font=("Arial", 10))
website_label.grid(column=0, row=1)
website_entry = Entry()
website_entry.grid(column=1, row=1, columnspan=2, sticky="EW")
website_entry.focus()

#email label
email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)
email_entry = Entry()
email_entry.grid(column=1, row=2, columnspan=2, sticky="EW")
email_entry.insert(END, string="pepsi.popser@gmail.com")

#password label
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)
password_entry = Entry()
password_entry.grid(column=1, row=3, sticky="EW")
password_generator_button = Button(text="Generate Password", command=random_password)
password_generator_button.grid(column=2, row=3, sticky="EW")

#add button
add_button = Button(text="Add", width=35, command=save)
add_button.grid(column=1, row=4, columnspan=2, sticky="EW")


window.mainloop()