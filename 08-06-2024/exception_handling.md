# Exception Handling in Python

Exception handling in Python is a mechanism to handle runtime errors, ensuring that the program continues to run smoothly despite encountering an error. It helps in managing errors gracefully without crashing the program.

## Basic Concepts

### 1. Exceptions

- **Exceptions** are events that disrupt the normal flow of a program's instructions.
- When an error occurs within a program, Python raises an exception.
- If the exception is not handled, the program will terminate with an error message.

### 2. Exception Handling

- **Exception handling** allows the program to continue execution or handle the error gracefully.
- Python provides a structured way to handle exceptions using `try`, `except`, `else`, and `finally` blocks.

## Syntax

```python
try:
    # Code that might raise an exception
except SomeException as e:
    # Code that runs if the exception occurs
else:
    # Code that runs if no exception occurs
finally:
    # Code that always runs, regardless of an exception
```

## Examples

### 1. Basic Exception Handling

```python
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print("Error:", e)
# Output: Error: division by zero
```

### 2. Multiple Exceptions

```python
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print("Error: Division by zero")
except TypeError as e:
    print("Error: Invalid data type")
# Output: Error: Division by zero
```

### 3. Catching All Exceptions

```python
try:
    result = 10 / 0
except Exception as e:
    print("Error:", e)
# Output: Error: division by zero
```

### 4. Using Else

- The `else` block runs if no exceptions occur.

```python
try:
    result = 10 / 2
except ZeroDivisionError as e:
    print("Error:", e)
else:
    print("Result:", result)
# Output: Result: 5.0
```

### 5. Finally Block

- The `finally` block always executes, regardless of whether an exception occurred or not.
- It's useful for cleanup actions, like closing files or releasing resources.

```python
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print("Error:", e)
finally:
    print("This block always executes")
# Output: Error: division by zero
#         This block always executes
```

## Custom Exceptions

- You can define your own exceptions by creating a class that inherits from the built-in `Exception` class.

### Example

```python
class CustomError(Exception):
    pass

try:
    raise CustomError("This is a custom error")
except CustomError as e:
    print("Caught a custom exception:", e)
# Output: Caught a custom exception: This is a custom error
```

## Exception Hierarchy

- Python exceptions are organized into a hierarchy.
- The `BaseException` is the base class for all exceptions.
- `Exception` is the base class for all built-in, non-exit exceptions.

### Common Exception Classes

- `ArithmeticError`: Base class for errors occurring during numeric calculations.
- `ZeroDivisionError`: Raised when division by zero occurs.
- `TypeError`: Raised when an operation or function is applied to an object of inappropriate type.
- `ValueError`: Raised when a function receives an argument of the right type but inappropriate value.
- `IndexError`: Raised when attempting to access an index that is out of range.
- `KeyError`: Raised when attempting to access a dictionary key that does not exist.
- `FileNotFoundError`: Raised when a file or directory is requested but doesn’t exist.

## Exceptions in details
Here's an explanation of some common types of exceptions in Python:

### 1. `SyntaxError`

- **Meaning**: A `SyntaxError` is raised when Python encounters code that violates the language's syntax rules.
- **Cause**: This can happen due to mistakes such as incorrect indentation, invalid syntax, or missing colons or parentheses.
- **Example**: 
  ```python
  try:
      if x == 5
          print("x is equal to 5")
  except SyntaxError:
      print("SyntaxError occurred")
  ```
- **Explanation**: In this example, the missing colon after the `if` statement causes a `SyntaxError`.

### 2. `IndentationError`

- **Meaning**: An `IndentationError` occurs when there is incorrect indentation in the code.
- **Cause**: Python uses indentation to define code blocks, so proper indentation is crucial.
- **Example**:
  ```python
  try:
      def my_function():
          print("Inside function")
           print("This line is incorrectly indented")  # Extra space
  except IndentationError:
      print("IndentationError occurred")
  ```
- **Explanation**: The extra space before the `print` statement inside the function causes an `IndentationError`.

### 3. `NameError`

- **Meaning**: A `NameError` is raised when Python encounters an undefined or unassigned variable or function name.
- **Cause**: This typically occurs when referencing a variable or function that hasn't been defined or is out of scope.
- **Example**:
  ```python
  try:
      print(x)  # x is not defined
  except NameError:
      print("NameError occurred")
  ```
- **Explanation**: In this example, attempting to print the value of an undefined variable `x` raises a `NameError`.

### 4. `TypeError`

- **Meaning**: A `TypeError` is raised when an operation or function is applied to an object of an inappropriate type.
- **Cause**: This occurs when attempting operations that are not supported by the data type.
- **Example**:
  ```python
  try:
      x = "hello"
      y = 5
      print(x + y)  # Cannot concatenate a string and an integer
  except TypeError:
      print("TypeError occurred")
  ```
- **Explanation**: Concatenating a string and an integer raises a `TypeError`.

### 5. `ValueError`

- **Meaning**: A `ValueError` is raised when a function receives an argument of the correct type but an inappropriate value.
- **Cause**: This occurs when passing invalid values to functions.
- **Example**:
  ```python
  try:
      int("hello")  # The string "hello" cannot be converted to an integer
  except ValueError:
      print("ValueError occurred")
  ```
- **Explanation**: Trying to convert the string "hello" to an integer raises a `ValueError`.

### 6. `ZeroDivisionError`

- **Meaning**: A `ZeroDivisionError` is raised when an attempt is made to divide a number by zero.
- **Cause**: Division by zero is mathematically undefined.
- **Example**:
  ```python
  try:
      x = 10
      y = 0
      result = x / y  # Division by zero is not allowed
  except ZeroDivisionError:
      print("ZeroDivisionError occurred")
  ```
- **Explanation**: Dividing a number by zero raises a `ZeroDivisionError`.



## Raising Exceptions

- You can raise exceptions using the `raise` keyword.

### Example

```python
def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero")
    return x / y

try:
    divide(10, 0)
except ValueError as e:
    print("Error:", e)
# Output: Error: Cannot divide by zero
```

## Using Assertions

- Assertions are a debugging aid that tests a condition.
- If the condition is `False`, it raises an `AssertionError`.

### Example

```python
x = -1
assert x >= 0, "x must be non-negative"
# Output: AssertionError: x must be non-negative
```

## Best Practices

### 1. Be Specific with Exceptions

- Catch specific exceptions rather than using a generic `except` block.

### 2. Use Finally for Cleanup

- Use the `finally` block to clean up resources such as file handles or network connections.

### 3. Avoid Bare Except

- Avoid using bare `except` clauses as they can catch unexpected exceptions and hide bugs.

### 4. Raise Meaningful Exceptions

- Raise meaningful exceptions with informative error messages.

### 5. Log Exceptions

- Log exceptions for better debugging and monitoring.

### Example of a Well-Structured Exception Handling

```python
import logging

logging.basicConfig(level=logging.INFO)

def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError as e:
        logging.error("Division by zero", exc_info=True)
        raise ValueError("Cannot divide by zero") from e
    else:
        return result
    finally:
        logging.info("Execution completed")

try:
    divide(10, 0)
except ValueError as e:
    print("Handled error:", e)
# Output:
# ERROR:root:Division by zero
# Traceback (most recent call last):
#   ...
# ZeroDivisionError: division by zero
# INFO:root:Execution completed
# Handled error: Cannot divide by zero
```
