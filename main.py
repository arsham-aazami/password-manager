from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password manager")
window.config(padx=20, pady=20)
window.minsize(530, 600)
logo_image = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=logo_image)
canvas.grid(row=0, column=1)

# Labels

website_label = Label(text="Website:", font=("Arial", 12, "normal"))
website_label.grid(row=1, column=0)
email_label = Label(text="Email:", font=("Arial", 12, "normal"))
email_label.grid(row=2, column=0)
password_label = Label(text="Password:", font=("Arial", 12, "normal"))
password_label.grid(row=3, column=0)


# Entries
website_entry = Entry(textvariable="Enter website url", width=35)
website_entry.grid(row=1, column=1, columnspan=2)
email_entry = Entry(textvariable="Enter website url", width=35)
email_entry.grid(row=2, column=1, columnspan=2)
password_entry = Entry(textvariable="Enter website url", width=21)
password_entry.grid(row=3, column=1)
password_generate_button = Button(text="Generate password")
password_generate_button.grid(row=3, column=2)
add_button = Button(text="Add", width=36)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()