import tkinter as tk
from tkinter import messagebox

# Function to handle button click
def on_button_click():
    print("Button clicked!")
    messagebox.showinfo("Information", "Button was clicked!")

# Create the main application window
root = tk.Tk()

# Set the title of the window
root.title("Basic Tkinter Window")

# Set the size of the window
root.geometry("200x200")

# Create a label widget
label = tk.Label(root, text="Hello, World!", font=("monospace", 16), fg="seagreen")
label.pack(pady=20)

# Create a button widget
button = tk.Button(root, text="Click Me", command=on_button_click)
button.pack(pady=10)

# Run the application
root.mainloop()
