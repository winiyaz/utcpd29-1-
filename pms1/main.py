from tkinter import *

# -- Color Constants
MAINBG = "#020617"
TEXTFG = "#EEE4B1"
ENTRYBG = "#1E201E"
ENTRYFG = "#F97300"
BUTTONBG = "#180161"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Panty Manager')
window.configure(bg=MAINBG, padx=100, pady=100)

# --- Setup Canvas

canvas = Canvas(height=200, width=200, highlightthickness=0)
logo_img = PhotoImage(file="n.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1, pady=20)

# - Labels

website_label = Label(text="Website  ", bg=MAINBG, fg=TEXTFG, font=('Arial', 20))
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username  ", bg=MAINBG, fg=TEXTFG, font=('Arial', 20))
email_label.grid(row=2, column=0)
password_label = Label(text="Password  ", bg=MAINBG, fg=TEXTFG, font=('Arial', 20))
password_label.grid(row=3, column=0)

# Entries
website_entry = Entry(width=35, bg=ENTRYBG, fg=ENTRYFG, font=('Courier', 20), insertbackground="hotpink", justify="center")
website_entry.grid(row=1, column=1, pady=5, columnspan=2, ipady=10)
email_entry = Entry(width=35, bg=ENTRYBG, fg=ENTRYFG, font=('Courier', 20), insertbackground="hotpink", justify="center")
email_entry.grid(row=2, column=1, pady=5, columnspan=2, ipady=10)
password_entry = Entry(width=30, bg=ENTRYBG, fg=ENTRYFG, font=('Courier', 20), insertbackground="hotpink", justify="center")
password_entry.grid(row=3, column=1, pady=5, ipady=10)

# Buttons
generate_password_button = Button(text="Sniff", font=('Arial', 15), bg=BUTTONBG, fg=ENTRYFG)
generate_password_button.grid(row=3, column=2)
add_button = Button(text="ADD", font=('Arial', 15), bg=BUTTONBG, fg=ENTRYFG, width=46)
add_button.grid(row=4, column=1, pady=20, columnspan=2)

# -- Window Setup ---
window.mainloop()
