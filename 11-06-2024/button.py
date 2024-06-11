import tkinter as tk
from tkinter import messagebox

def button_clicked():
    messagebox.showinfo("Hello", "You are cute!")

# Create the main window
root = tk.Tk()
root.title("Cute Button")

# Set window size and position
root.geometry("300x150+500+300")

# Set window background color
root.configure(bg="lightblue")

# Create a button widget
button = tk.Button(root, text="Click Me!", command=button_clicked, bg="pink", fg="black", font=("Georgia", 14, 'bold'), width=15,activebackground='lemon chiffon')

# Place the button on the window
button.pack(pady=20)

# Run the Tkinter event loop
root.mainloop()
