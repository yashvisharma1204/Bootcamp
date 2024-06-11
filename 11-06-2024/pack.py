import tkinter as tk

root = tk.Tk()
root.title("Pack Example")

label_1 = tk.Label(root, text="Label 1", bg="lightblue")
label_1.pack(fill=tk.BOTH, padx=10, pady=10)

label_2 = tk.Label(root, text="Label 2", bg="lightgreen")
label_2.pack(fill=tk.BOTH, padx=10, pady=10)

label_3 = tk.Label(root, text="Label 3", bg="lightcoral")
label_3.pack(fill=tk.BOTH, padx=10, pady=10)


root.mainloop()
