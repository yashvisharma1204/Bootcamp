import tkinter as tk
from tkinter import messagebox

# Function to show a cute aesthetic message box
def show_aesthetic_message():
    title = "🌸 Message 🌸"
    message = "Your presence in this kaleidoscopic labyrinth of existence is truly captivating. 🌟"
    messagebox.showinfo(title, message)

root = tk.Tk()
root.title("Aesthetic Message Box")
root.config(background='indian red')
button = tk.Button(root, text="Show Message", command=show_aesthetic_message)
button.pack(pady=20)

root.mainloop()
