from tkinter import *
from tkinter import messagebox


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_datas():

	website_name = website_entry.get()
	user_email = email_entry.get()
	user_password = password_entry.get()

	if len(website_name) == 0 or len(user_email) == 0 or len(user_password) == 0:
		messagebox.showinfo(title="alert", message="NO filed should be empty!")
	else:
		is_message_answer_true = messagebox.askyesno(title="pop-up", message="Do you want to save your logged information?")
		if is_message_answer_true:
			with open("saved_data.txt", mode="a") as file:
				file.write(f"{website_name} | {user_email} | {user_password} \n")
				email_entry.delete(0, END)
				# user_email.delete(0, END)
				user_password.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password manager")
window.config(padx=50, pady=50)
# window.minsize(530, 600)
logo_image = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=logo_image)
canvas.grid(row=0, column=1)

# Labels

website_label = Label(text="Website:", font=("Arial", 12, "normal"))
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:", font=("Arial", 12, "normal"))
email_label.grid(row=2, column=0)
password_label = Label(text="Password:", font=("Arial", 12, "normal"))
password_label.grid(row=3, column=0)

# Entries
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "arsham@gmail.com")
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)
password_generate_button = Button(text="Generate password")
password_generate_button.grid(row=3, column=2)
add_button = Button(text="Add", width=36, command=save_datas)
add_button.grid(row=4, column=1, columnspan=2)

print(website_entry.get())
window.mainloop()
