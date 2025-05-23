from tkinter import *
from tkinter import messagebox

import pyperclip

import passgenarator

FONT = ("Ariel", 12, "normal")

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    gene_password = passgenarator.generate_password()
    password_entry.insert(0,f"{gene_password}")
    pyperclip.copy(password_entry.get())
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website_name = website_entry.get()
    if website_entry.get() and email_entry.get() and password_entry.get():
        with open("data.txt", "a") as file:
            file.write(f"{website_entry.get()} | {email_entry.get()} | {password_entry.get()} " + "\n")
            website_entry.delete(0,END)
            password_entry.delete(0, END)
            messagebox.showinfo(title="data saved", message=f"Password for {website_name} have bin saved")
    else:
        messagebox.showerror(title="Error", message="Input all data")
# ---------------------------- UI SETUP ------------------------------- #

windows = Tk()
windows.title("Password Manager")
windows.config(padx=50,pady=50)
################################ Canvas Image
canvas = Canvas(height=200,width=200)
key_image = PhotoImage(file="logo.png")

canvas.create_image(100,100 ,image=key_image)
canvas.grid(row=0,column=1)
############################### Web site Label and entry
website_label = Label(text="Website", font=FONT)
website_label.grid(row=2,column=0)

website_entry = Entry(width=29)
website_entry.focus()
website_entry.grid(row=2,column=1,columnspan=2)
############################### Email/Username label and entry
email_username_label = Label(text="Email/Username:", font=FONT)
email_username_label.grid(row=3,column=0)

email_entry = Entry(width=29)
email_entry.insert(0,"Mehdi_fadae@yahoo.com")
email_entry.grid(row=3,column=1,columnspan=2)
############################### Password label and entry and button
password_label = Label(text="Password: ", font=FONT)
password_label.grid(row=4,column=0)

password_entry = Entry(width=15)
password_entry.grid(row=4,column=1)

password_button = Button(text="Generate", command=generate_password)
password_button.grid(row=4,column=2)

############################### Add Button
add_button = Button(text="Add",width=27, command=save)
add_button.grid(row=5,column=1,columnspan=2)



windows.mainloop()