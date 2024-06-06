# Functions in Python

# Definition: Functions are essential for structuring code, enabling reusability, and promoting modularity. 
# They break down complex tasks into smaller, more manageable parts.

# Syntax: Functions are defined using the def keyword, followed by the function name and parentheses containing parameters (if any). 
# The function body is indented and contains the behavior of the function.

# Example:

def greet(name):
    """This function prints a greeting message."""
    print("Hello", name + "!")

# Function call
greet("J")
# Output: Hello J!

# Parameters in Functions
# Positional Arguments: Passed to the function based on their position in the function call.

# Example:

def greet_person(greeting, name):
    """This function greets a person using a custom greeting."""
    print(greeting, name + "!")

# Function call with positional arguments
greet_person("Hello", "Alice")
# Output: Hello Alice!

# Default Arguments: Have predefined values and are used when no value is provided during the function call.

# Example:

def greet(name, message="Hello"):
    """This function greets someone with an optional message."""
    print(message, name + "!")

# Function call with default argument
greet("Bob")  # Output: Hello Bob!

# Function call with custom argument
greet("Alice", "Hi")  # Output: Hi Alice!

# Variable Length Arguments (*args): Allow functions to accept an arbitrary number of arguments.

# Example:

def calculate_sum(*args):
    """This function calculates the sum of all arguments."""
    total = 0
    for num in args:
        total += num
    return total

# Function call with variable length arguments
result = calculate_sum(1, 2, 3, 4, 5)
print("Sum:", result)  # Output: Sum: 15

# Lambda Function

# Anonymous Functions: Defined using the lambda keyword, allowing for concise function definitions.
# Concise: Ideal for short, single-expression operations.

# Example:

add = lambda x, y: x + y
result = add(5, 3)
print("Result of addition:", result)  # Output: Result of addition: 8

# Map, Reduce, and Filter

# Functional Programming: Provide powerful tools for processing sequences.
# Map: Applies a function to all elements of an iterable.
# Filter: Selects elements based on a condition.
# Reduce: Applies a function cumulatively to elements of an iterable (less commonly used).

# Example:

# Map: Squaring each number in a list
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x * x, numbers))
print("Squared Numbers:", squared_numbers)  # Output: Squared Numbers: [1, 4, 9, 16, 25]

# Filter: Selecting even numbers from a list
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Even Numbers:", even_numbers)  # Output: Even Numbers: [2, 4]

# Reduce: Calculating the product of all numbers in a list
from functools import reduce
product = reduce(lambda x, y: x * y, numbers)
print("Product:", product)  # Output: Product: 120

# Local and Global Variables

# Scope: Defines the accessibility of variables within code.
# Local Variables: Defined within a function and accessible only within that function.
# Global Variables: Declared outside functions and accessible throughout the code.

# Example:

x = 10  # Global variable

def my_function():
    y = 20  # Local variable
    print("Inside function:", x, y)

print("Outside function:", x)
my_function()

# Return Statement

# Purpose: Exits a function and optionally sends a value back to the caller.
# Single/Multiple Values: Can return a single value or multiple values packed into a tuple.

# Example:

def square(x):
    """This function squares a number."""
    return x * x

result = square(5)
print("Square of 5:", result)  # Output: 25