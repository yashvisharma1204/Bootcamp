![Screenshot 2024-06-12 142651](https://github.com/yashvisharma1204/Bootcamp/assets/137611141/cc8ad0c2-1fb3-4258-bc51-c9c0976e360b)### Tkinter Listbox Notes

#### Overview:
The `Listbox` widget in Tkinter is used to display a list of items from which a user can select one or more items.

#### Syntax:
```python
w = Listbox(master, option, ...)
```

#### Parameters:
- **master**: This represents the parent window.
- **options**: These are key-value pairs separated by commas that configure the widget.

#### Commonly Used Options:
1. **bg**: The normal background color displayed behind the label and indicator.
2. **bd**: The size of the border around the indicator. Default is 2 pixels.
3. **cursor**: The cursor that appears when the mouse is over the listbox.
4. **font**: The font used for the text in the listbox.
5. **fg**: The color used for the text in the listbox.
6. **height**: Number of lines (not pixels!) shown in the listbox. Default is 10.
7. **highlightcolor**: Color shown in the focus highlight when the widget has the focus.
8. **highlightthickness**: Thickness of the focus highlight.
9. **relief**: Selects three-dimensional border shading effects. The default is SUNKEN.
10. **selectbackground**: The background color to use when displaying selected text.
11. **width**: The width of the widget in characters. The default is 20.
12. **xscrollcommand**: If you want to allow the user to scroll the listbox horizontally, you can link your listbox widget to a horizontal scrollbar.
13. **yscrollcommand**: If you want to allow the user to scroll the listbox vertically, you can link your listbox widget to a vertical scrollbar.
14. **selectmode**: Determines how many items can be selected, and how mouse drags affect the selection:
    - **BROWSE**: Normally, you can only select one line out of a listbox. If you click on an item and then drag to a different line, the selection will follow the mouse. This is the default.
    - **SINGLE**: You can only select one line, and you can't drag the mouse. Wherever you click button 1, that line is selected.
    - **MULTIPLE**: You can select any number of lines at once. Clicking on any line toggles whether or not it is selected.
    - **EXTENDED**: You can select any adjacent group of lines at once by clicking on the first line and dragging to the last line.

#### Methods:
1. **activate(index)**: Selects the line specified by the given index.
2. **curselection()**: Returns a tuple containing the line numbers of the selected element or elements, counting from 0. If nothing is selected, returns an empty tuple.
3. **delete(first, last=None)**: Deletes the lines whose indices are in the range `[first, last]`. If the second argument is omitted, the single line with index `first` is deleted.
4. **get(first, last=None)**: Returns a tuple containing the text of the lines with indices from `first` to `last`, inclusive. If the second argument is omitted, returns the text of the line closest to `first`.
5. **index(i)**: If possible, positions the visible part of the listbox so that the line containing index `i` is at the top of the widget.
6. **insert(index, *elements)**: Insert one or more new lines into the listbox before the line specified by `index`. Use `END` as the first argument if you want to add new lines to the end of the listbox.
7. **nearest(y)**: Return the index of the visible line closest to the y-coordinate `y` relative to the listbox widget.
8. **see(index)**: Adjust the position of the listbox so that the line referred to by `index` is visible.
9. **size()**: Returns the number of lines in the listbox.
10. **xview()**: To make the listbox horizontally scrollable, set the command option of the associated horizontal scrollbar to this method.
11. **xview_moveto(fraction)**: Scroll the listbox so that the leftmost fraction of the width of its longest line is outside the left side of the listbox. Fraction is in the range `[0,1]`.
12. **xview_scroll(number, what)**: Scrolls the listbox horizontally. For the `what` argument, use either `UNITS` to scroll by characters, or `PAGES` to scroll by pages, that is, by the width of the listbox. The `number` argument tells how many to scroll.
13. **yview()**: To make the listbox vertically scrollable, set the command option of the associated vertical scrollbar to this method.
14. **yview_moveto(fraction)**: Scroll the listbox so that the top fraction of the width of its longest line is outside the left side of the listbox. Fraction is in the range `[0,1]`.
15. **yview_scroll(number, what)**: Scrolls the listbox vertically. For the `what` argument, use either `UNITS` to scroll by lines, or `PAGES` to scroll by pages, that is, by the height of the listbox. The `number` argument tells how many to scroll.

![Screenshot 2024-06-12 142651](https://github.com/yashvisharma1204/Bootcamp/assets/137611141/92fae375-daf5-4a00-b5a3-3796499868bf)
