# Python basics
# Arithmetic Calculator
# Write a Python program that takes two numbers as input from the user and performs arithmetic operations 
# (addition, subtraction, multiplication, division, floor division, modulus, and exponentiation) on them. 
# Display the results for each operation.

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("Addition:", num1 + num2)
print("Subtraction:", num1 - num2)
print("Multiplication:", num1 * num2)
print("Division:", num1 / num2)
print("Floor Division:", num1 // num2)
print("Modulus:", num1 % num2)
print("Exponentiation:", num1 ** num2)


# Check Odd or Even
# Write a Python program that takes an integer input from the user and checks if it's odd or even. 
# Print the result accordingly.

number = int(input("Enter an integer: "))

if number % 2 == 0:
    print("Even")
else:
    print("Odd")


# String Manipulation
# Write a Python program that takes a string input from the user and performs the following operations:
# - Count the number of vowels and consonants in the string.
# - Convert the string to uppercase and print it.
# - Replace all spaces with underscores ('_') and print the modified string.

string = input("Enter a string: ")
vowels = 0
consonants = 0

for char in string:
    if char.lower() in 'aeiou':
        vowels += 1
    elif char.isalpha():
        consonants += 1

print("Number of vowels:", vowels)
print("Number of consonants:", consonants)
print("Uppercase string:", string.upper())
print("Modified string with underscores:", string.replace(' ', '_'))


# Temperature Converter
# Write a Python program that converts temperature units. The program should:
# - Take a temperature value and unit (Celsius or Fahrenheit) as input from the user.
# - Convert the temperature to the other unit and display the result.

temp_value = float(input("Enter temperature value: "))
temp_unit = input("Enter temperature unit (Celsius or Fahrenheit): ")

if temp_unit.lower() == 'celsius':
    converted_temp = (temp_value * 9/5) + 32
    print("Temperature in Fahrenheit:", converted_temp)
elif temp_unit.lower() == 'fahrenheit':
    converted_temp = (temp_value - 32) * 5/9
    print("Temperature in Celsius:", converted_temp)
else:
    print("Invalid temperature unit.")


# Factorial Calculator
# Write a Python program that calculates the factorial of a given number using a while loop. 
# Prompt the user to enter a positive integer and calculate its factorial.

number = int(input("Enter a positive integer: "))
factorial = 1
if number < 0:
    print("Factorial is not defined for negative numbers.")
elif number == 0:
    print("Factorial of 0 is 1")
else:
    while number > 0:
        factorial *= number
        number -= 1
    print("Factorial:", factorial)

# Python Functions
# 10.1. Area Calculator:

def calculate_area(shape, dimensions):
    if shape == "rectangle":
        length, width = dimensions
        return length * width
    elif shape == "circle":
        radius = dimensions[0]
        return 3.14 * radius * radius  # Approximation of pi
    else:
        return "Invalid shape specified."

# Test cases
print("Area of rectangle:", calculate_area("rectangle", (5, 3)))  # Output: 15
print("Area of circle:", calculate_area("circle", (4,)))  # Output: 50.24


# 10.2. String Manipulation:

def reverse_words(text):
    words = text.split()
    reversed_words = [word[::-1] for word in words]
    return ' '.join(reversed_words)

# Test case
print("Reversed words:", reverse_words("Hello World"))  # Output: olleH dlroW


# 10.3. List Statistics:

def analyze_list(numbers):
    stats = {}
    stats["Minimum"] = min(numbers)
    stats["Maximum"] = max(numbers)
    stats["Average"] = sum(numbers) / len(numbers)
    return stats

# Test case
print("Statistics:", analyze_list([1, 2, 3, 4, 5]))  # Output: {'Minimum': 1, 'Maximum': 5, 'Average': 3.0}


# 10.4. Filtering with Lambda:

def filter_short_names(names, max_length):
    return list(filter(lambda x: len(x) < max_length, names))

# Test case
product_names = ["Apple", "Banana", "Orange", "Grape", "Pineapple"]
print("Short names:", filter_short_names(product_names, 6))  # Output: ['Apple', 'Banana', 'Grape']


# 10.5. Text Analyzer (Bonus Challenge):

def analyze_text(text):
    words = text.lower().split()
    word_count = len(words)
    char_count = sum(len(word) for word in words)
    word_freq = {}
    for word in words:
        word_freq[word] = word_freq.get(word, 0) + 1
    most_frequent_word = max(word_freq, key=word_freq.get)
    return {"Word Count": word_count, "Character Count": char_count, "Most Frequent Word": most_frequent_word}

# Test case
text = "This is a sample text to analyze. This text contains words. Words are important."
print("Text Analysis:", analyze_text(text))  # Output: {'Word Count': 11, 'Character Count': 61, 'Most Frequent Word': 'this'}
