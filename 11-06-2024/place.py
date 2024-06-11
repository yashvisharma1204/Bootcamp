import tkinter as tk

root = tk.Tk()
root.title("Place Example")

# Using Place Manager
label_1 = tk.Label(root, text="Label 1", bg="lightblue")
label_1.place(x=50, y=50)

label_2 = tk.Label(root, text="Label 2", bg="lightgreen")
label_2.place(x=150, y=100)

label_3 = tk.Label(root, text="Label 3", bg="lightcoral")
label_3.place(x=100, y=200)


root.mainloop()
