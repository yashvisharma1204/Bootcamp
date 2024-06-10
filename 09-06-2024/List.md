# Lists

Python Lists are the fundamental data structure that allows you to store a collection of items in a specific order and are just like dynamically sized arrays.

- **Ordered**: Lists maintain the order of their elements. The first item you add stays at index 0, the second at index 1, and so on.
- **Indexable**: You can access elements by their index, using square brackets. The first element has index 0, the second index 1, etc.
- **Mutable**: Lists can be modified after they are created. You can add, remove, or change elements within a list.
- **Heterogeneous**: Lists can contain different types of elements. You can mix integers, strings, floats, and even other lists.
- **Dynamic**: Lists can grow and shrink as needed. You can append elements to a list, remove them, or extend the list with other lists.
- **Iterable**: Lists can be looped through (iterated over), allowing you to perform operations on each element in the list.
- **Methods and Functions**: Lists have a variety of built-in methods and functions for common operations like append, insert, remove, pop, sort, reverse, index, count, extend, and more.

### List Methods

- **Append**: Adds a single element to the end of a list.
- **Insert**: Inserts a new element at a specified position within the list.
- **Remove**: Removes the first occurrence of a specified element from the list.
- **Copy (shallow and deep copy)**: Creates copies of lists. A shallow copy creates a new list object but still refers to the original elements. A deep copy creates a new list as well as new copies of the elements within it.
- **Count**: Returns the number of occurrences of a specified element within the list.
- **Extend**: Appends elements from another iterable (such as another list) to the end of the current list.
- **Index**: Returns the index of the first occurrence of a specified element within the list.
- **Sort**: Sorts the elements of the list in ascending order (by default) or in a specified order.
- **Reverse**: Reverses the order of the elements in the list.
- **Clear**: Removes all elements from the list, leaving it empty.
- **Pop**: Removes and returns the element at the specified position in the list. If no index is specified, it removes and returns the last element.

```python
# Sample list to work with
fruits = ["apple", "banana", "cherry"]

# Append
fruits.append("orange")
print(f"Append: {fruits}")

# Insert
fruits.insert(1, "grape")
print(f"Insert: {fruits}")

# Remove
fruits.remove("banana")
print(f"Remove: {fruits}")

# Copy
# Shallow Copy
fruits_shallow_copy = fruits.copy()
fruits_shallow_copy[0] = "lemon"  
print(f"Shallow Copy: {fruits_shallow_copy}, Original: {fruits}")

# Deep Copy
import copy
fruits_deep_copy = copy.deepcopy(fruits)
fruits_deep_copy[0] = "kiwi"  
print(f"Deep Copy: {fruits_deep_copy}, Original: {fruits}")

# Count
fruits.append("apple")
apple_count = fruits.count("apple")
print(f"Count of 'apple': {apple_count}")

# Extend
more_fruits = ["pear", "pineapple"]
fruits.extend(more_fruits)
print(f"Extend: {fruits}")

# Index
apple_index = fruits.index("apple")
print(f"Index of 'apple': {apple_index}")

# Sort
fruits.sort() 
print(f"Sort: {fruits}")

# Reverse
fruits.reverse()
print(f"Reverse: {fruits}")

# Clear
fruits.clear()
print(f"Clear: {fruits}")

# Pop
removed_fruit = more_fruits.pop()  
print(f"Pop: {removed_fruit}, Remaining: {more_fruits}")
```

### List Comprehension

List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.

```python
# List of squares for numbers from 0 to 9
squares = [x ** 2 for x in range(10)]
print("List of squares:", squares)

# List of even numbers from 0 to 19
even_numbers = [x for x in range(20) if x % 2 == 0]
print("Even numbers:", even_numbers)

# List of words converted to uppercase
words = ["hello", "world", "python", "code"]
uppercased_words = [word.upper() for word in words]
print("Uppercased words:", uppercased_words)

# List of tuples with numbers and their squares
number_square_pairs = [(x, x ** 2) for x in range(10)]
print("Number-Square pairs:", number_square_pairs)

# Flattened list from a list of lists
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened_list = [item for sublist in nested_list for item in sublist]
print("Flattened list:", flattened_list)
```

### Indexing

Positive and negative indexing, retrieving, updating elements.

```python
# Create a list of fruits
fruits = ["apple", "banana", "cherry", "date", "elderberry"]

# Accessing elements using positive indexing
first_fruit = fruits[0]  
second_fruit = fruits[1] 
last_fruit = fruits[-1]  
print("First fruit:", first_fruit)  
print("Second fruit:", second_fruit) 
print("Last fruit:", last_fruit)  

# Accessing elements using negative indexing
second_last_fruit = fruits[-2] 
third_last_fruit = fruits[-3]  
print("Second last fruit:", second_last_fruit)  
print("Third last fruit:", third_last_fruit)  

# Get the value of an element at a specific index
middle_fruit = fruits[2]  
print("Middle fruit:", middle_fruit)  

# Change the value of an element at a specific index
fruits[1] = "blueberry"  
print("Updated fruits:", fruits) 
```

### Slicing

Positive and negative slicing, retrieving, updating, deleting elements, inserting elements.

```python
# Create a list of fruits
fruits = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape"]

# Slice from index 1 to 4 
subset1 = fruits[1:4]  
print("Positive Slicing:", subset1)

# Slice with a step
subset2 = fruits[1:6:2]  
print("Positive Slicing with Step:", subset2)

# Slice the last three elements
subset3 = fruits[-3:] 
print("Negative Slicing:", subset3)

# Slice from the second to last to the fourth to last 
subset4 = fruits[-2:-5:-1]  
print("Negative Slicing with Reverse:", subset4)

# Extract a portion of the list
middle_subset = fruits[2:5]  
print("Retrieve a Portion:", middle

_subset)

# Update elements within a slice
fruits[1:3] = ["blueberry", "cranberry"]  
print("Update a Slice:", fruits)  

# Remove elements within a slice
del fruits[2:4]  
print("Delete a Slice:", fruits)  

# Add elements into a specific position
fruits[1:1] = ["kiwi", "mango"]  
print("Insert into a Slice:", fruits)  
```

### Basic searching and sorting in list

Searching for elements and sorting the list.

```python
# Create a list of fruits
fruits = ["apple", "banana", "cherry", "date", "elderberry"]

# Checking if an element exists in the list
has_banana = "banana" in fruits  
print("Is 'banana' in the list?", has_banana)

# Finding the index of an element
banana_index = fruits.index("banana")  
print("Index of 'banana':", banana_index)

# Iterating through the list to find a specific element
element_to_find = "date"
found_element = None
for fruit in fruits:
    if fruit == element_to_find:
        found_element = fruit
        break
print("Found element:", found_element)  

```

### Special Methods

Using special methods like `reduce`, `map`, `filter`, `zip` for advanced list operations.

```python
from functools import reduce

# Sum of a list of numbers using reduce
numbers = [1, 2, 3, 4, 5]
sum_result = reduce(lambda x, y: x + y, numbers)  
print("Sum using reduce:", sum_result)

# Finding the maximum value in a list using reduce
max_result = reduce(lambda x, y: x if x > y else y, numbers)  
print("Max value using reduce:", max_result)

# Convert a list of numbers to their squares using map
squares = list(map(lambda x: x ** 2, [1, 2, 3, 4, 5])) 
print("Squares using map:", squares)

# Convert a list of strings to their uppercase forms
words = ["apple", "banana", "cherry"]
uppercased = list(map(str.upper, words)) 
print("Uppercased words using map:", uppercased)

# Filter a list to get only even numbers
even_numbers = list(filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5, 6])) 
print("Even numbers using filter:", even_numbers)

# Filter a list to get words with more than 5 letters
long_words = list(filter(lambda word: len(word) > 5, ["apple", "banana", "cherry", "date", "elderberry"])) 
print("Long words using filter:", long_words)

# Zip two lists to create pairs of elements
fruits = ["apple", "banana", "cherry"]
quantities = [10, 20, 30]
fruit_quantities = list(zip(fruits, quantities))  
print("Zipped lists:", fruit_quantities)

# Zip three lists
colors = ["red", "yellow", "red"]
fruit_colors_quantities = list(zip(fruits, colors, quantities)) 
print("Zipped three lists:", fruit_colors_quantities)
```

### Practice Questions

```python
# List for Practice
fruits = ["apple", "banana", "cherry", "date", "elderberry"]

# Q1: Basic Operations with Lists
# Add a new fruit "fig" to the end of the list
fruits.append("fig")
print("Q1.1 - After appending 'fig':", fruits)

# Insert "grape" at the 2nd position (index 1)
fruits.insert(1, "grape")
print("Q1.2 - After inserting 'grape' at index 1:", fruits)

# Remove the first occurrence of "banana"
fruits.remove("banana")
print("Q1.3 - After removing 'banana':", fruits)

# Return the first and last element of the list
first_fruit = fruits[0]
last_fruit = fruits[-1]
print("Q1.4 - First and last fruit:", first_fruit, last_fruit)
```

### More Practice Questions

```python
# Q2: Indexing and Slicing
# Get the third fruit from the list
third_fruit = fruits[2]
print("Q2.1 - Third fruit:", third_fruit)

# Retrieve a slice containing the first three fruits
first_three_fruits = fruits[:3]
print("Q2.2 - First three fruits:", first_three_fruits)

# Retrieve a slice containing the last two fruits using negative indexing
last_two_fruits = fruits[-2:]
print("Q2.3 - Last two fruits:", last_two_fruits)

# Update the second fruit to "blueberry"
fruits[1] = "

blueberry"
print("Q2.4 - After updating the second fruit:", fruits)
```

```python
# Q3: List Methods and Functions
numbers = [1, 2, 3, 4, 5]

# Append the number 6 to the list
numbers.append(6)
print("Q3.1 - After appending 6:", numbers)

# Insert the number 0 at the beginning of the list
numbers.insert(0, 0)
print("Q3.2 - After inserting 0 at the beginning:", numbers)

# Remove and return the last element from the list
last_element = numbers.pop()
print("Q3.3 - Last element popped:", last_element, "Remaining list:", numbers)

# Return the count of occurrences of the number 2
count_2 = numbers.count(2)
print("Q3.4 - Count of '2':", count_2)

# Return the index of the number 3
index_3 = numbers.index(3)
print("Q3.5 - Index of '3':", index_3)

# Reverse the order of the list
numbers.reverse()
print("Q3.6 - After reversing:", numbers)
```

```python
# Q4: List Comprehensions
# Create a list of even numbers from 0 to 20
even_numbers = [x for x in range(21) if x % 2 == 0]
print("Q4.1 - Even numbers:", even_numbers)

# Create a list of squares of numbers from 1 to 10
squares = [x ** 2 for x in range(1, 11)]
print("Q4.2 - Squares from 1 to 10:", squares)

# Create a list of uppercase words from a list
words = ["hello", "world", "python", "lists"]
uppercased = [word.upper() for word in words]
print("Q4.3 - Uppercased words:", uppercased)

# Create a flattened list from a nested list
nested = [[1, 2], [3, 4], [5, 6]]
flattened = [item for sublist in nested for item in sublist]
print("Q4.4 - Flattened list from nested list:", flattened)
```

```python
# Q5: Searching and Sorting
# Check if "cherry" is in the list of fruits
has_cherry = "cherry" in fruits
print("Q5.1 - Is 'cherry' in the list?", has_cherry)

# Find the index of "date" in the list
date_index = fruits.index("date")
print("Q5.2 - Index of 'date':", date_index)

# Sort the list of fruits in ascending order
fruits.sort()
print("Q5.3 - Fruits sorted in ascending order:", fruits)

# Sort the list of fruits in descending order
fruits.sort(reverse=True)
print("Q5.4 - Fruits sorted in descending order:", fruits)
```

```python
# Q6: Special Methods
from functools import reduce

# Calculate the sum of the list using `reduce`
numbers = [1, 2, 3, 4, 5]
total_sum = reduce(lambda x, y: x + y, numbers)
print("Q6.1 - Sum of numbers using reduce:", total_sum)

# Create a list of cubes of numbers using `map`
cubes = list(map(lambda x: x ** 3, numbers))
print("Q6.2 - Cubes of numbers using map:", cubes)

# Filter out the odd numbers from a list
even_only = list(filter(lambda x: x % 2 == 0, numbers))
print("Q6.3 - Even numbers using filter:", even_only)

# Zip two lists to create pairs of names and scores
names = ["Alice", "Bob", "Charlie"]
scores = [95, 87, 92]
name_score_pairs = list(zip(names, scores))
print("Q6.4 - Zipped names and scores:", name_score_pairs)
