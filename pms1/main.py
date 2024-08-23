from tkinter import *

# -- Color Constants
MAINBG = "#020617"
TEXTFG = "#EEE4B1"
ENTRYBG = "#344955"
ENTRYFG = "#FFFED3"
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
canvas.grid(row=0, column=1)

# - Labels
website_label = Label(text="Website  ", bg=MAINBG, fg=ENTRYFG, font=('Arial', 20))
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username  ", bg=MAINBG, fg=ENTRYFG, font=('Arial', 20))
email_label.grid(row=2, column=0)
password_label = Label(text="Password  ", bg=MAINBG, fg=ENTRYFG, font=('Arial', 20))
password_label.grid(row=3, column=0)

# Entries
website_entry = Entry(width=35, bg=ENTRYBG, fg=ENTRYFG, font=('Arial', 20))
website_entry.grid(row=1, column=1, pady=10, columnspan=2)
email_entry = Entry(width=35, bg=ENTRYBG, fg=ENTRYFG, font=('Arial', 20))
email_entry.grid(row=2, column=1, pady=10, columnspan=2)
password_entry = Entry(width=30, bg=ENTRYBG, fg=ENTRYFG, font=('Arial', 20))
password_entry.grid(row=3, column=1, pady=10)

# Buttons
generate_password_button = Button(text="Sniff", font=('Arial', 15), bg=BUTTONBG, fg=ENTRYFG, width=10)
generate_password_button.grid(row=3, column=2, padx=30)
add_button = Button(text="ADD", font=('Arial', 15), bg=BUTTONBG, fg=ENTRYFG, width=10)
add_button.grid(row=4, column=1, padx=30, pady=20)

# -- Window Setup ---
window.mainloop()
