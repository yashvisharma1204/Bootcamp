import tkinter as tk
from tkinter import messagebox


def check_artist_name():
    if entry_var.get().strip().lower() == "new jeans":
        messagebox.showinfo("Result", "You are right!")
    else:
        messagebox.showwarning("Result", "Wrong answer, try again!")

# Create the main application window
root = tk.Tk()
root.title("Album Artist Guessing Game")
root.geometry('350x550')

album_cover = tk.PhotoImage(file="getup.png")  # Make sure to replace with your image file path
album_label = tk.Label(root, image=album_cover)
album_label.pack(pady=10)
question_label = tk.Label(root, text="Do you like this album? \nIf yes, which artist's album is this?", font=("Helvetica", 14))
question_label.pack(pady=10)

# StringVar to hold the text of the entry field
entry_var = tk.StringVar()

entry = tk.Entry(root, textvariable=entry_var, bd=3, bg="skyblue", fg="black", font=("Georgia", 14), width=20, relief="sunken")
entry.pack(pady=20)

submit_button = tk.Button(root, text="Submit", command=check_artist_name, font=("Georgia", 14),relief='raised',bg='seagreen3')
submit_button.pack(pady=10)

root.mainloop()
