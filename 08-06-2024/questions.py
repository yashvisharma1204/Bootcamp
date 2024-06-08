#Question 1
#Write a function that takes two numbers as input and divides the first number by the second number. Raise a ZeroDivisionError if the second number is zero.
def divide_numbers(num1, num2):
    if num2 == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    else:
        result = num1 / num2
        return result

# Example usage
try:
    print(divide_numbers(10, 2))  # Output: 5.0
    print(divide_numbers(5, 0))   # Raises ZeroDivisionError
except ZeroDivisionError:
    print("Error: Division by zero is not allowed")

#Question 2
#Create a function that checks if a given string is a palindrome. Raise a custom PalindromeError if the input is not a valid string.

class PalindromeError(Exception):
    pass

def is_palindrome(input_str):
    if not isinstance(input_str, str):
        raise PalindromeError("Input must be a string")

    # Remove spaces and convert to lowercase
    clean_str = input_str.replace(" ", "").lower()

    # Check if the string is equal to its reverse
    if clean_str == clean_str[::-1]:
        return True
    else:
        return False

# Example usage
try:
    print(is_palindrome("racecar"))  # Output: True
    print(is_palindrome("A man a plan a canal Panama"))  # Output: True
    print(is_palindrome(123))  # Raises PalindromeError
except PalindromeError as e:
    print(e)

#Question 3
#Write a Python script that iterates through a list of integers and attempts to divide each integer by zero. Handle the ZeroDivisionError exception within a try-except block, and use a finally block to print a message indicating the end of the iteration process.
numbers = [10, 0, 5, 20, 3]

for num in numbers:
    try:
        result = num / 0
        print(f"{num} / 0 = {result}")
    except ZeroDivisionError:
        print(f"Error: Cannot divide {num} by zero")
    finally:
        print("Iteration completed")
        print("-----------------------")

print("End of script")