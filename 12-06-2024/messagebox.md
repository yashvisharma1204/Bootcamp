### Tkinter tkMessageBox Notes

#### Overview:
The `tkMessageBox` module in Tkinter is used to display message boxes in applications. It provides several functions to display different types of messages or prompts for user interaction.

#### Syntax:
```python
tkMessageBox.FunctionName(title, message [, options])
```

#### Parameters:
- **FunctionName**: This is the name of the appropriate message box function.
- **title**: This is the text to be displayed in the title bar of the message box.
- **message**: This is the text to be displayed as a message.
- **options**: These are alternative choices that you may use to tailor a standard message box. Some of the options that you can use are `default` and `parent`. The `default` option is used to specify the default button (e.g., ABORT, RETRY, or IGNORE) in the message box. The `parent` option is used to specify the window on top of which the message box is to be displayed.

#### Available Functions:
You can use one of the following functions with dialogue boxes:
- **showinfo()**: Displays an informational message.
- **showwarning()**: Displays a warning message.
- **showerror()**: Displays an error message.
- **askquestion()**: Asks a question with a Yes/No answer.
- **askokcancel()**: Asks for confirmation with OK/Cancel options.
- **askyesno()**: Asks for confirmation with Yes/No options.
- **askretrycancel()**: Asks for confirmation with Retry/Cancel options.
![Screenshot 2024-06-12 142436](https://github.com/yashvisharma1204/Bootcamp/assets/137611141/95163723-1f75-42a1-82fc-a7abbf05fad5)
![Screenshot 2024-06-12 142424](https://github.com/yashvisharma1204/Bootcamp/assets/137611141/af97aadd-49a6-41af-a802-c907b72bb979)
