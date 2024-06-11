# Tkinter Entry

The `Entry` widget is used to create a single-line text input field in a Python application. It allows users to enter and edit a single line of text.

## Syntax:

Here is the simple syntax to create this widget-

```python
e = Entry(master, option=value, ...)
```

### Parameters:

- **master**: This represents the parent window.

- **options**: A set of key-value pairs for configuring the widget's appearance and behavior.

# Options available and their description

1. **bd**: Border width in pixels. Default is 2.

2. **bg**: Background color of the entry field.

3. **command**: Function to be called when the state of the entry field changes.

4. **fg**: Foreground (text) color of the entry field.

5. **font**: Text font to be used for the entry field.

6. **highlightcolor**: The color of the focus highlight when the widget has focus.

7. **justify**: How to align the text: LEFT, CENTER, or RIGHT.

8. **relief**: Relief specifies the type of the border. Some of the values are SUNKEN, RAISED, GROOVE, and RIDGE.

9. **show**: This is used to display a string in the entry field instead of the actual characters, commonly used for passwords (e.g., `show="*"`).

10. **state**: Set this option to DISABLED to make the entry field uneditable. Default is NORMAL.

11. **width**: Width of the entry field in characters.

12. **validate**: Specifies when the `validatecommand` should be called. Can be FOCUS, KEY, or ALL.

13. **validatecommand**: A command that gets called to validate the input.

14. **textvariable**: A variable that is associated with the entry widget, which gets updated with the entry's current text.

# Methods

## delete(first, last=None):
Deletes characters from the entry field. The `first` argument specifies the starting index, and the optional `last` argument specifies the ending index.

## get():
Returns the current text in the entry field.

## insert(index, string):
Inserts a string at the specified index in the entry field.

## flash():
Causes the entry field to flash several times between active and normal colors. Ignored if the entry is disabled.

## icursor(index):
Sets the insertion cursor to the specified index.

## index(index):
Returns the numerical index of the specified text index.

## invoke():
Calls the entry's callback function, if defined.

## select_adjust(index):
Adjusts the end of the selection near the specified index.

## select_clear():
Clears the selection if there is one.

## select_from(index):
Set the anchor point of the selection at the specified index.

## select_present():
Returns `True` if there is a selection, `False` otherwise.

## select_range(start, end):
Selects text from the `start` index to the `end` index.

## select_to(index):
Selects text from the anchor point to the specified index.

## xview(index):
Scrolls the entry horizontally to make the specified text index visible.

## xview_scroll(number, what):
Scrolls the entry horizontally by the specified number of `what` units.
<br>
<img width="257" alt="image" src="https://github.com/yashvisharma1204/Bootcamp/assets/137611141/add25297-3e60-44b1-b8ca-d91e3b1c404a">

