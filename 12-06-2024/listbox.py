import tkinter as tk

root = tk.Tk()
root.title("Cute List Box Example")

# Create a list box
listbox = tk.Listbox(root, width=30, height=10, bg="pink1", fg="#333333", font=("Georgia", 12,'bold'))

cute_items = ["🐱 Kitty", "🐶 Puppy", "🌸 Flower", "🍦 Ice Cream", "🎈 Balloon"]
for item in cute_items:
    listbox.insert(tk.END, item)

listbox.pack(pady=20, padx=10)

root.mainloop()
