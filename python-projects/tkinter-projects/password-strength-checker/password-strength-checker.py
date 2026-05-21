import tkinter as tk
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import string
import random
import re
import hashlib
import customtkinter as ctk

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

# Create GUI window
window = ctk.CTk()
window.title("Password Strength Checker")
window.geometry("560x400")
window.configure(fg_color="#191f27")

icon = tk.PhotoImage(
    file="images/shield.png")
window.iconphoto(False, icon)

visible = False
strength_value = 0

# Functions


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


def suggest_password(password):
    suggestions = []
    if not re.search(r"[A-Z]", password):
        suggestions.append(random.choice(string.ascii_uppercase))
    if not re.search(r"[a-z]", password):
        suggestions.append(random.choice(string.ascii_lowercase))
    if not re.search(r"[0-9]", password):
        suggestions.append(random.choice(string.digits))
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        suggestions.append(random.choice("!@#$%^&*()"))
    while len(password) + len(suggestions) < 8:
        suggestions.append(random.choice(
            string.ascii_letters + string.digits + "!@#$%^&*()"))
    return password + ''.join(suggestions)


def check_password():
    password = entry.get()

    upper_case = any(1 if c in string.ascii_uppercase else 0 for c in password)
    lower_case = any(1 if c in string.ascii_lowercase else 0 for c in password)
    specical = any(1 if c in string.punctuation else 0 for c in password)
    digits = any(1 if c in string.digits else 0 for c in password)

    characters = [upper_case, lower_case, specical, digits]

    length = len(password)
    global strength_value

    strength = 0

    password_strength_label.grid(
        row=5, column=0, columnspan=2, padx=(60, 0), pady=10)
    suggestion_label.grid(row=6, column=0, columnspan=2, padx=(50, 0), pady=5)
    common_password_label.grid(row=7, column=0, columnspan=2, padx=(50, 0))

    # checks if the password is found in common passwords list
    with open('files/common.txt', 'r') as f:
        common = f.read().splitlines()

    if password in common:
        common_password_label.configure(
            text="password was found in common list; Try another password!")

    if length >= 12:
        strength += 2
    elif length >= 8:
        strength += 1

    if sum(characters) > 0:
        strength += 1
    if sum(characters) > 1:
        strength += 1
    if sum(characters) > 2:
        strength += 1
    if sum(characters) > 3:
        strength += 1

    if strength <= 2:
        password_strength_label.configure(
            text="Weak Password", text_color="red")
        bar.set(0.25)
        suggession = suggest_password(password)
        suggestion_label.configure(text=f"Suggestion: {suggession}")
    elif strength <= 4:
        password_strength_label.configure(
            text="Moderate Password", text_color="orange")
        bar.set(0.5)
        suggestion_label.configure(
            text="Try adding  symbols or numbers to improve strength")
        common_password_label.grid_forget()
    elif strength <= 5:
        password_strength_label.configure(
            text="Strong Password", text_color="green")
        bar.set(0.75)
        suggestion_label.configure(text="")
        common_password_label.grid_forget()
    else:
        password_strength_label.configure(
            text="Very Strong Password", text_color="blue")
        bar.set(1)
        suggestion_label.configure(text="Excellent Password")
        common_password_label.grid_forget()

    strength_value = strength


def on_toggle_save():
    password = entry.get()

    if not password:
        messagebox.showwarning("Empty", "Enter password first")
        return

    if save_var.get() and strength_value >= 4:
        hashed = hash_password(password)

        with open("files/password.txt", "a") as file:
            file.write(hashed + "\n")

        messagebox.showinfo("Saved", "Password saved securely!")

    elif save_var.get() and strength_value < 4:
        messagebox.showwarning(
            "Weak Password", "Password must be at least Strong to save")


def reset():
    entry.delete(0, END)
    suggestion_label.grid_forget()
    password_strength_label.grid_forget()
    common_password_label.grid_forget()
    bar.set(0)


def toggle():
    global visible
    if visible:
        entry.configure(show="*")
        button_hide.configure(image=eye_open)
        visible = False
    else:
        entry.configure(show="")
        button_hide.configure(image=eye_closed)
        visible = True


# Title label
head_text = ctk.CTkLabel(
    window,
    text="Enter Your Password!",
    font=("Arial", 18)
)
head_text.grid(row=0, column=0, columnspan=3, padx=170, pady=10)

# Define and Display input field
entry = ctk.CTkEntry(
    window,
    width=460,
    placeholder_text="Type password...",
    corner_radius=5
)
entry.grid(row=1, column=0, columnspan=4, padx=(20, 0), pady=10)

eye_open = ctk.CTkImage(Image.open(
    "images/visible.png"), size=(22, 22))
eye_closed = ctk.CTkImage(Image.open(
    "images/hidden.png"), size=(22, 22))

button_hide = ctk.CTkButton(
    window, text="", image=eye_open, width=20, corner_radius=(5), command=toggle)
button_hide.grid(row=1, column=2, padx=(0, 20))

# Define and Display checkbox
save_var = ctk.BooleanVar(master=window, value=False)
checkbox = ctk.CTkCheckBox(
    master=window, text="Save Password Securely", variable=save_var, command=lambda: on_toggle_save())
checkbox.grid(row=3, column=0, columnspan=3, pady=20)

# Define Buttons
button_submit = ctk.CTkButton(
    window,
    text="Check Strength",
    width=140,
    fg_color="#3498db",
    hover_color="#2980b9",
    cursor="hand2",
    command=check_password
)

button_reset = ctk.CTkButton(
    window,
    text="Reset",
    width=100,
    fg_color="#3498db",
    hover_color="#2980b9",
    cursor="hand2",
    command=reset
)

# Disaply Buttons
button_submit.grid(row=2, column=0, padx=(120, 10), pady=10)
button_reset.grid(row=2, column=1, padx=(10, 120), pady=10)

# Define, Define and set to 0(initially) for strength bar
bar = ctk.CTkProgressBar(window, width=400, fg_color="grey")
bar.grid(row=4, column=0, columnspan=3, pady=10)

bar.set(0)  # start empty

# Define password strength labels
password_strength_label = ctk.CTkLabel(
    window, text="")
password_strength_label.grid(
    row=5, column=0, columnspan=2, padx=(60, 0), pady=10)

# Define suggesion labe
suggestion_label = ctk.CTkLabel(window, text="")
suggestion_label.grid(row=6, column=0, columnspan=2, padx=(50, 0), pady=5)

# Define and Display common password
common_password_label = ctk.CTkLabel(
    window, text="", text_color="pink")
common_password_label.grid(row=7, column=0, columnspan=2, padx=(50, 0))


# Make Loop
window.mainloop()
