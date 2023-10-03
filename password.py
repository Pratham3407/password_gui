import tkinter as tk
from tkinter import ttk, messagebox
import string
import random

def generate_password():
    length = int(length_entry.get())
    
    if length < 8:
        messagebox.showwarning("Password Length", "Password should be at least 8 characters long.")
        return
    
    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(chars) for _ in range(length))
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)
    
    strength = "Weak" if length < 12 else "Strong"
    strength_label.config(text=f"Password Strength: {strength}")

def save_password():
    password = password_entry.get()
    with open('passwords.txt', 'a') as file:
        file.write(password + '\n')
    messagebox.showinfo("Saved", "Password saved successfully.")

def toggle_password_visibility():
    if show_password_var.get():
        password_entry.config(show='')
    else:
        password_entry.config(show='*')

# GUI Setup
root = tk.Tk()
root.title("Password Generator")

style = ttk.Style()
style.configure('TButton', font=('Arial', 12))

frame = ttk.Frame(root, padding="20")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

length_label = ttk.Label(frame, text="Password Length:")
length_label.grid(row=0, column=0, sticky=tk.W, pady=(0,5))

length_entry = ttk.Entry(frame)
length_entry.grid(row=0, column=1, pady=(0,5))

generate_button = ttk.Button(frame, text="Generate Password", command=generate_password)
generate_button.grid(row=1, column=0, columnspan=2, pady=(0,10))

password_label = ttk.Label(frame, text="Generated Password:")
password_label.grid(row=2, column=0, sticky=tk.W, pady=(0,5))

password_entry = ttk.Entry(frame, show='*')
password_entry.grid(row=2, column=1, pady=(0,5))

show_password_var = tk.BooleanVar()
show_password_checkbox = ttk.Checkbutton(frame, text="Show Password", variable=show_password_var, command=toggle_password_visibility)
show_password_checkbox.grid(row=3, column=0, columnspan=2, pady=(0,10))

save_button = ttk.Button(frame, text="Save Password", command=save_password)
save_button.grid(row=4, column=0, columnspan=2, pady=(0,10))

strength_label = ttk.Label(frame, text="Password Strength:")
strength_label.grid(row=5, column=0, columnspan=2)

root.mainloop()
