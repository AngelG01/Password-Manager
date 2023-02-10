import json
from tkinter import *
from tkinter import messagebox
import random

# Search for information about a certain website: 
def search_for_info():
    key = website_entry.get()
    try:
        with open('data.json', 'r') as file:
            data = json.load(file)

            if key in data.keys():
                username, password = data[key]['username'], data[key]['password']
                messagebox.showinfo(title='Message', message=f'Username: {username}\nPassword: {password}')
            else:
                messagebox.showinfo(title='Message', message='No website info')
    except FileNotFoundError:
        messagebox.showinfo(title='Message', message='No website info')


# Password Generator:
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers

    random.shuffle(password_list)

    password = "".join(password_list)
    return password_entry.insert(0, password)


# Save data to a file:
def save_data():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            'username': username,
            'password': password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title='Oops', message='Make sure you filled all the boxes.')
    else:
        is_ok = messagebox.askokcancel(title=website,
                                       message=f'These are the details entered: \nWebsite: {website}\nUsername: {username}\nPassword: {password}')

        if is_ok:
            try:
                with open('data.json', 'r') as file:
                    data = json.load(file)
            except FileNotFoundError:
                with open('data.json', 'w') as file:
                    json.dump(new_data, file, indent=4)
            else:
                data.update(new_data)
                with open('data.json', 'w') as file:
                    json.dump(data, file, indent=4)

                website_entry.delete(0, END)
                password_entry.delete(0, END)


## Create GUI:

window = Tk()
window.title('Password Manager')
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
our_logo_img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=our_logo_img)
canvas.grid(row=0, column=1)

# Labels
website_label = Label(text='Website:')
website_label.grid(row=1, column=0)
username_label = Label(text='Email/Username:')
username_label.grid(row=2, column=0)
password_label = Label(text='Password:')
password_label.grid(row=3, column=0)

# Entries
website_entry = Entry(width=36)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()

username_entry = Entry(width=36)
username_entry.grid(row=2, column=1, columnspan=2)
username_entry.insert(0, 'example@gmail.com')

password_entry = Entry(width=25)
password_entry.grid(row=3, column=1, sticky=E)

# Buttons
generate_password_button = Button(text='Generate password!', command=generate_password)
generate_password_button.grid(row=3, column=2)

add_button = Button(text='Add', width=30, command=save_data)
add_button.grid(row=4, column=1, columnspan=2)

search_button = Button(text='Search', command=search_for_info)
search_button.grid(row=1, column=2, sticky=E)

window.mainloop()
