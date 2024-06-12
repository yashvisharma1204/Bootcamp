import tkinter as tk
from tkinter import colorchooser
from PIL import ImageGrab

def choose_color():
    color = colorchooser.askcolor()[1]
    if color:
        global current_color
        current_color = color

def clear_canvas():
    canvas.delete("all")

def save_canvas():
    canvas.update()
    x = root.winfo_rootx() + canvas.winfo_x()
    y = root.winfo_rooty() + canvas.winfo_y()
    x1 = x + canvas.winfo_width()
    y1 = y + canvas.winfo_height()
    ImageGrab.grab().crop((x, y, x1, y1)).save("drawing.png")

def paint(event):
    x1, y1 = (event.x - 1), (event.y - 1)
    x2, y2 = (event.x + 1), (event.y + 1)
    canvas.create_oval(x1, y1, x2, y2, fill=current_color, outline=current_color)

root = tk.Tk()
root.title("Simple Drawing Application")

current_color = "black"

button_frame = tk.Frame(root, bg="lightgrey")
button_frame.pack(fill=tk.X)

color_button = tk.Button(button_frame, text="Choose Color", command=choose_color)
color_button.pack(side=tk.LEFT, padx=5, pady=5)

clear_button = tk.Button(button_frame, text="Clear", command=clear_canvas)
clear_button.pack(side=tk.LEFT, padx=5, pady=5)

save_button = tk.Button(button_frame, text="Save", command=save_canvas)
save_button.pack(side=tk.LEFT, padx=5, pady=5)

canvas = tk.Canvas(root, bg="white", width=600, height=400)
canvas.pack(expand=True, fill=tk.BOTH)

canvas.bind("<B1-Motion>", paint)

root.mainloop()
