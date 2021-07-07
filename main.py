from tkinter import *
from tkinter import messagebox
import random
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def pass_gen():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    pass_letters = [random.choice(letters) for _ in range(random.randint(8, 12))]
    pass_numbers = [random.choice(numbers) for _ in range(random.randint(3, 5))]
    pass_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    combined = pass_letters + pass_numbers + pass_symbols
    password = ''.join(combined)

    password_entry.insert(0, password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    web_data = website_entry.get()
    email_data = email_entry.get()
    password_data = password_entry.get()
    is_ok = False
    if len(web_data) == 0 or len(password_data) == 0 or len(email_data) == 0:
        messagebox.showinfo(title="oops!", message="Hey! Don't Leave any box empty!")
    else:
        is_ok = messagebox.askokcancel(title=web_data, message=f"Your given data:\nE-mail: {email_data}\nPassword: {password_data}\nIs everything ok?")

    if is_ok:
        # alternative : data_file = open("data.txt",'a')
        with open("data.txt", 'a') as data_file:
            data_file.write(f"{web_data} | {email_data} | {password_data} \n")
            website_entry.delete(0, END)
            password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()

window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=300)
logoimage = PhotoImage(file="logo.png")
canvas.create_image(150, 150, image=logoimage)
canvas.grid(row=0, column=1)


# LABELS
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

# ENTRIES

website_entry = Entry(width=70)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()

email_entry = Entry(width=70)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "example@email.com")

password_entry = Entry(width=50)
password_entry.grid(row=3, column=1)

# BUTTON
generate_button = Button(text="Generate Password",  command=pass_gen)
generate_button.grid(row=3, column=2)

save_button = Button(text="Add", width=60, command=save)
save_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
