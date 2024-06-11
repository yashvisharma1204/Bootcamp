import tkinter as tk

def main():
    # Create the main window
    root = tk.Tk()
    root.title("Tkinter Label Example")
    root.geometry('200x200')

    # Create and configure a label
    label = tk.Label(root, 
                     text="Hello!", 
                     bg="RoyalBlue2", 
                     fg="White", 
                     font=("georgia", 16), 
                     padx=20, 
                     pady=10,
                     relief="sunken", 
                     borderwidth=5,
                     justify='center')
    
    # Place the label on the window
    label.pack(pady=60)

    # Run the application
    root.mainloop()


main()