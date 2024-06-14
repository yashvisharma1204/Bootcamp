import tkinter as tk

def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, str(current) + str(number))

def clear():
    entry.delete(0, tk.END)

def evaluate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

root = tk.Tk()
root.title("Calculator")
root.geometry('365x370')

entry = tk.Entry(root, width=20, font=("georgia", 20), relief="flat", bg="#f0f0f0", fg="#333")
entry.grid(row=1, column=0, columnspan=4, padx=10, pady=10)

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', '=', '+'
]

row = 2
col = 0
for button in buttons:
    if button == '=':
        tk.Button(root, text=button, width=5, height=2, font=("Georgia", 15), command=evaluate, bg="#A7E7F3", fg="#000").grid(row=row, column=col, padx=5, pady=5)
    elif button == 'C':
        tk.Button(root, text=button, width=5, height=2, font=("Georgia", 15), command=clear, bg="#E7F3A7", fg="#000").grid(row=row, column=col, padx=5, pady=5)
    else:
        tk.Button(root, text=button, width=5, height=2, font=("Georgia", 15), command=lambda x=button: button_click(x), bg="#F3A7E7", fg="#333",).grid(row=row, column=col, padx=5, pady=5)
    
    col += 1
    if col > 3:
        col = 0
        row += 1

root.configure(bg="#F3A7E7")
root.mainloop()
