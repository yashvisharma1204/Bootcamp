import tkinter as tk

root = tk.Tk()
root.title("Form Layout Example")
root.geometry('300x200')

main_frame = tk.Frame(root, bg="white", bd=3, relief="ridge")
main_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)


form_frame = tk.Frame(main_frame, bg="mediumpurple", bd=2, relief="flat")
form_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=5, pady=5)

button_frame = tk.Frame(main_frame, bg="LightGoldenrod1", bd=2, relief="groove")
button_frame.pack(side=tk.BOTTOM, fill=tk.X, padx=5, pady=5)


tk.Label(form_frame, text="Name:", bg="mediumpurple").grid(row=0, column=0, padx=5, pady=5)
tk.Entry(form_frame).grid(row=0, column=1, padx=5, pady=5)
tk.Label(form_frame, text="Email:", bg="mediumpurple").grid(row=1, column=0, padx=5, pady=5)
tk.Entry(form_frame).grid(row=1, column=1, padx=5, pady=5)


tk.Button(button_frame, text="Submit", bg='mediumpurple2').pack(side=tk.LEFT, padx=10, pady=10)
tk.Button(button_frame, text="Cancel", bg='mediumpurple2').pack(side=tk.RIGHT, padx=10, pady=10)


root.mainloop()
