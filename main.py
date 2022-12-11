import random
from required_datas import *
from tkinter import *
from tkinter import messagebox


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generat_password():
		
	num_of_letters = random.randint(8,10)
	num_of_numbers = random.randint(2, 4)
	num_of_symbols = random.randint(2, 4)

	generated_letter = ""
	generated_numbers = ""
	generated_symbols = ""

	# defining a function to get random letter, number and symbols
	def generating_letter_numbers_symbols(num_char, char_set, generated_char):
		"""Take the number of characters of the specified set of words, numbers, symbols"""
		for number in range(num_char):
			random_char = random.choice(char_set)
			generated_char += random_char
			
		return generated_char


	l = generating_letter_numbers_symbols(num_of_letters, letters, generated_letter)
	n = generating_letter_numbers_symbols(num_of_numbers, numbers, generated_numbers)
	s = generating_letter_numbers_symbols(num_of_symbols, symbols, generated_symbols)

	# total_code = l + n + s
	# implementing all cases and permutaion for (letters),(numbers) and (symbols)
	sit1 = l + n + s
	sit2 = l + s + n
	sit3 = n + l + s
	sit4 = n + s + l
	sit5 = s + l + n
	sit6 = s + n + l


	code_randomization_list = [sit1, sit2, sit3, sit4, sit5, sit6]
	random_generated_code = random.choice(code_randomization_list)
	password_entry.insert(0, random_generated_code) 


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
password_generate_button = Button(text="Generate password", command=generat_password)
password_generate_button.grid(row=3, column=2)
add_button = Button(text="Add", width=36, command=save_datas)
add_button.grid(row=4, column=1, columnspan=2)

print(website_entry.get())
window.mainloop()
