# Python Input and Output Statements

# Input statement
# The input() function prompts the user to enter input, which is returned as a string. The prompt argument is optional but can be used to display a message to the user.
name = input("Enter your name: ")
print("Hello,", name)

# Output statement with keyword arguments
# The print() function outputs one or more arguments to the standard output. 
# The sep argument specifies the separator between arguments (default is a space).
# The end argument specifies what to print at the end (default is a newline character).
print("Hello", "World", sep=", ", end="!\n")

# Data Types in Python

# Numeric Types
# int: Represents integers. Example: 10
# float: Represents floating-point numbers. Example: 3.14
# complex: Represents complex numbers. Example: 2 + 3j
int_num = 42
float_num = 9.81
complex_num = 1 + 2j

# Sequence Types
# str: Represents strings. Example: "Hello, World!"
# list: Represents ordered, mutable collections. Example: [1, 2, 3, 4, 5]
# tuple: Represents ordered, immutable collections. Example: (1, 2, 3, 4, 5)
string = "Python Programming"
list_example = ["apple", "banana", "cherry"]
tuple_example = ("car", "bike", "boat")

# Mapping Type
# dict: Represents a collection of key-value pairs. Keys must be unique and immutable. Example: {"name": "John", "age": 30}
dict_example = {"city": "New York", "country": "USA"}

# Set Types
# set: Represents an unordered collection of unique elements. Example: {1, 2, 3, 4, 5}
# frozenset: An immutable version of a set. Example: frozenset({1, 2, 3, 4, 5})
set_example = {"apple", "banana", "cherry"}

# Boolean Type
# bool: Represents truth values. Example: True or False
boolean = False

# Expressions and Operators

a = 15
b = 4

# Arithmetic Operators
# + : Addition. Example: 15 + 4 = 19
# - : Subtraction. Example: 15 - 4 = 11
# * : Multiplication. Example: 15 * 4 = 60
# / : Division. Example: 15 / 4 = 3.75
# // : Floor Division (quotient without remainder). Example: 15 // 4 = 3
# % : Modulus (remainder). Example: 15 % 4 = 3
# ** : Exponentiation. Example: 15 ** 4 = 50625
print(a + b)  
print(a - b)  
print(a * b)  
print(a / b)  
print(a // b) 
print(a % b)  
print(a ** b) 

# Comparison Operators
# == : Equal to. Example: 15 == 4 -> False
# != : Not equal to. Example: 15 != 4 -> True
# >  : Greater than. Example: 15 > 4 -> True
# <  : Less than. Example: 15 < 4 -> False
# >= : Greater than or equal to. Example: 15 >= 4 -> True
# <= : Less than or equal to. Example: 15 <= 4 -> False
print(a == b)
print(a != b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)

# Logical Operators
# and : Returns True if both operands are true. Example: (15 > 5 and 4 < 5) -> True
# or  : Returns True if at least one operand is true. Example: (15 > 5 or 4 < 1) -> True
# not : Returns True if the operand is false. Example: not(15 > 5 and 4 < 5) -> False
print(a > 5 and b < 5)
print(a > 5 or b < 1)
print(not(a > 5 and b < 5))

# Type Casting
# Converting data from one type to another.

# int() converts to integer, truncating the decimal part.
int_from_float = int(9.81)  # 9

# float() converts to floating-point number.
float_from_int = float(42)  # 42.0

# str() converts to string.
string_from_int = str(100)  # "100"

# list() converts to list.
list_from_string = list("Python")  # ['P', 'y', 't', 'h', 'o', 'n']

# tuple() converts to tuple.
tuple_from_list = tuple(["car", "bike", "boat"])  # ("car", "bike", "boat")

# set() converts to set.
set_from_list = set(["apple", "banana", "cherry"])  # {"apple", "banana", "cherry"}

print(int_from_float)
print(float_from_int)
print(string_from_int)
print(list_from_string)
print(tuple_from_list)
print(set_from_list)

# Conditional Statements

a = 20
b = 15

# if statement
# Executes a block of code if the specified condition is true.
if a > b:
    print(f"{a} is greater than {b}")
# elif statement
# Provides additional conditions to check if previous conditions were false.
elif a < b:
    print(f"{a} is less than {b}")
# else statement
# Specifies a block of code to execute if none of the previous conditions were true.
else:
    print(f"{a} is equal to {b}")

# Looping Statements

# For loop
# Used to iterate over sequences (like lists, tuples, strings) or other iterable objects.
colors = ["red", "green", "blue"]
for color in colors:
    print(color)

# While loop
# Executes a block of code as long as a specified condition is true.
count = 0
while count < 3:
    print(count)
    count += 1

# Jumping Statements

# break statement
# Terminates the current loop and transfers control to the next statement outside the loop.
for i in range(10):
    if i == 7:
        break
    print(i)

# continue statement
# Skips the current iteration of the loop and moves to the next iteration.
for i in range(10):
    if i == 7:
        continue
    print(i)

# Special Functions

# len()
# Returns the number of items in an object (e.g., the length of a string, list, tuple, or other iterable).
words = ["hello", "world", "python"]
print(len(words))  # Output: 3

# id()
# Returns the unique identifier (memory address) of an object.
print(id(words))  # Output: Unique ID of the list object

# type()
# Returns the type of an object (e.g., int, float, str, list, etc.).
print(type(words))  # Output: <class 'list'>

# range()
# Generates a sequence of numbers within a specified range and is commonly used in for loops.
for i in range(3):
    print(i)  # Output: 0 1 2