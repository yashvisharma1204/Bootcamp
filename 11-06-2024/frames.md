# Tkinter Frame Widget

## Introduction
The Frame widget in Tkinter is essential for grouping and organizing other widgets in a user-friendly manner. Acting as a container, it helps arrange the position of widgets and can serve as a base class for creating complex widgets.

## Creating a Frame
To create a Frame widget, use the following syntax:

```python
w = Frame(master, option=value, ...)
```

### Parameters:
- **master**: The parent window where the frame is placed.
- **options**: A set of key-value pairs to configure the frame's appearance and behavior.

## Common Options for Frame

### Background and Border
- **bg**: Sets the normal background color of the frame.
- **bd**: Specifies the border width in pixels. The default value is 2.

### Cursor and Dimensions
- **cursor**: Changes the mouse cursor when it hovers over the frame. Possible values include 'arrow', 'dot', etc.
- **height**: Sets the vertical dimension of the frame.
- **width**: Specifies the frame's width.

### Highlight and Relief
- **highlightbackground**: Color of the focus highlight when the frame does not have focus.
- **highlightcolor**: Color of the focus highlight when the frame has focus.
- **highlightthickness**: Thickness of the focus highlight border.
- **relief**: Defines the style of the frame's border. Possible values include `FLAT`, `SUNKEN`, `RAISED`, `GROOVE`, and `RIDGE`.

<img width="223" alt="image" src="https://github.com/yashvisharma1204/Bootcamp/assets/137611141/3572c996-968b-4721-9523-f52fb05d8f00">
