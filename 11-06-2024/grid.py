import tkinter as tk

# Create the main application window
root = tk.Tk()
root.title("Grid Example")

# Using Grid Manager
label_1 = tk.Label(root, text="Label 1", bg="lightblue")
label_1.grid(row=0, column=0, padx=10, pady=10)

label_2 = tk.Label(root, text="Label 2", bg="lightgreen")
label_2.grid(row=0, column=1, padx=10, pady=10)

label_3 = tk.Label(root, text="Label 3", bg="lightcoral")
label_3.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

# Real-life Analogy: Grid layout similar to a spreadsheet grid where each cell can contain different information.
# Each label in the grid represents a cell in the spreadsheet.
# The labels can be used to display various data or information in an organized manner.

# Run the application
root.mainloop()
