# Tkinter Text Widget

The `Text` widget in Tkinter is used to display and edit multi-line text. It's ideal for creating text editors or for displaying long-form text.

## Syntax

```python
text_widget = Text(master, options)
```

- **master**: The parent window or frame.
- **options**: Configuration options for the text widget.

## Common Options

1. **background (bg)**: Background color of the text area.
2. **foreground (fg)**: Color of the text.
3. **font**: Font type and size for the text.
4. **height**: Number of lines visible in the text widget.
5. **width**: Number of characters visible per line.
6. **wrap**: Controls text wrapping. Values can be `NONE`, `CHAR`, or `WORD`.
7. **state**: Normal or disabled state of the text widget.

## Key Methods

- **get(start, end)**: Retrieves text from the specified range.
- **insert(index, text)**: Inserts text at the specified index.
- **delete(start, end)**: Deletes text from the specified range.
- **tag_configure(tagname, options)**: Configures the appearance of text tags.

## Example Usage

This example demonstrates a basic usage of the `Text` widget, including adding and configuring text.

```python
import tkinter as tk

def submit_text():
    user_text = text.get("1.0", tk.END)
    print("User input:", user_text)

# Create the main application window
root = tk.Tk()
root.title("Tkinter Text Example")

# Create and configure a Text widget
text = tk.Text(root, height=10, width=50, font=("Helvetica", 12), wrap=tk.WORD, bg="lightgray", fg="black")
text.pack(pady=10)

# Create a submit button
submit_button = tk.Button(root, text="Submit", command=submit_text)
submit_button.pack(pady=10)

# Run the application
root.mainloop()
```

### Explanation

1. **Creating the Main Window**: Sets up the Tkinter window with the title "Tkinter Text Example".
2. **Text Widget**: 
   - `height=10`: The text area displays 10 lines of text.
   - `width=50`: Each line can hold 50 characters.
   - `wrap=tk.WORD`: Wraps text by word boundaries.
   - `bg="lightgray"`: Sets the background color to light gray.
   - `fg="black"`: Sets the text color to black.
3. **Submit Button**: 
   - When clicked, the button calls `submit_text` to print the text from the `Text` widget.
4. **submit_text Function**:
   - Retrieves text from the `Text` widget from the beginning ("1.0") to the end (`tk.END`).
   - Prints the retrieved text.

### Advanced Features

- **Tags**: Tags allow you to apply styles to specific text ranges.
  ```python
  text.tag_configure("highlight", background="yellow", foreground="red")
  text.insert(tk.END, "Highlighted Text", "highlight")
  ```
- **Binding Events**: You can bind events to the `Text` widget to trigger actions.
  ```python
  def on_key(event):
      print("Key pressed:", event.char)
      
  text.bind("<Key>", on_key)
  ```

### Conclusion

The `Text` widget is a powerful tool in Tkinter for handling multi-line text input and display. It supports various configurations and methods to manage and style text effectively.
