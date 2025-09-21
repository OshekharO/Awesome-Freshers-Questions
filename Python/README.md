# Python Basics Cheat Sheet 🐍📚

## Part 1: Data Types & Variables

### What is a Variable?
A named container that stores data values in memory for later use.

```python
name = "Alice"  # Variable 'name' stores the text "Alice"
age = 25        # Variable 'age' stores the number 25
```

### Common Python Data Types

| Type | Description | Example |
|------|-------------|---------|
| `str` | Text data (string of characters) | `message = "Hello, World"` |
| `int` | Whole numbers without decimals | `count = 42` |
| `float` | Numbers with decimal points | `price = 19.99` |
| `bool` | Logical values: True or False | `is_valid = True` |
| `list` | Ordered collection that can be changed | `fruits = ["apple", "banana", "cherry"]` |
| `tuple` | Ordered collection that cannot be changed | `coords = (10.5, 20.7)` |
| `set` | Unordered collection of unique items | `colors = {"red", "green", "blue"}` |
| `dict` | Collection of key-value pairs | `person = {"name": "Alice", "age": 25}` |

**Dynamic Typing**: Python automatically determines data types - no need to declare them.

---

## Part 2: Operators in Python ⚙️

### Arithmetic Operators (Perform mathematical operations)
```python
a = 10; b = 3
a + b   # Addition → 13
a - b   # Subtraction → 7
a * b   # Multiplication → 30
a / b   # Division → 3.33
a % b   # Modulus (remainder) → 1
a ** b  # Exponent (power) → 1000
a // b  # Floor Division (rounds down) → 3
```

### Comparison Operators (Compare values, return True/False)
```python
a == b  # Equal to
a != b  # Not equal to
a > b   # Greater than
a < b   # Less than
a >= b  # Greater than or equal to
a <= b  # Less than or equal to
```

### Logical Operators (Combine conditional statements)
```python
x = True; y = False
x and y  # AND - True if both are True → False
x or y   # OR - True if at least one is True → True
not x    # NOT - reverses the result → False
```

### Assignment Operators (Assign values to variables)
```python
x = 5    # Basic assignment
x += 3   # Add and assign → x = x + 3 → 8
x -= 2   # Subtract and assign → x = x - 2 → 6
x *= 2   # Multiply and assign → x = x * 2 → 12
x /= 3   # Divide and assign → x = x / 3 → 4.0
```

### Identity Operators (Check if objects are the same)
```python
x is y     # True if both variables point to same object
x is not y # True if variables point to different objects
```

### Membership Operators (Check if value exists in sequence)
```python
x in [1, 2, 3]     # True if value exists in sequence
x not in [1, 2, 3] # True if value doesn't exist in sequence
```

---

## Part 3: Control Flow 🔁

Control flow determines the order in which code executes based on conditions.

### Conditional Statements (Make decisions in code)
```python
age = 18
if age >= 18:
    print("You are an adult")
elif age > 13:
    print("You are a teenager")
else:
    print("You are a child")
```

### Loops (Repeat code multiple times)

**For Loop** (Iterate over a sequence):
```python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)  # Prints each fruit
```

**While Loop** (Execute while condition is true):
```python
count = 0
while count < 5:
    print(count)
    count += 1  # Increment count
```

### Loop Control Statements (Modify loop behavior)
- `break`: Exit the loop completely
- `continue`: Skip to next iteration
- `pass`: Do nothing (placeholder)

```python
for i in range(5):
    if i == 3:
        break  # Exit loop when i is 3
    print(i)   # Prints 0, 1, 2
```

---

## Part 4: Functions 🧩

Functions are reusable blocks of code that perform specific tasks.

### Defining a Function
```python
def greet(name):  # Function definition
    print(f"Hello, {name}!")  # Function body
```

### Calling a Function
```python
greet("Alice")  # Function call → "Hello, Alice!"
```

### Return Statement (Send back a value from function)
```python
def add(a, b):
    return a + b  # Returns the sum

result = add(3, 5)  # result = 8
```

### Default Parameters (Set default values)
```python
def greet(name="Guest"):  # Default value
    print(f"Hello, {name}")

greet()  # → "Hello, Guest"
```

### Keyword Arguments (Pass arguments by name)
```python
def info(name, age):
    print(f"{name} is {age} years old")

info(age=25, name="Bob")  # Arguments by name
```

### Variable-Length Arguments (Accept any number of arguments)
```python
def show_args(*args):    # Accepts any number of positional arguments
    print(args)          # Returns as tuple

def show_kwargs(**kwargs):  # Accepts any number of keyword arguments
    print(kwargs)           # Returns as dictionary
```

---

## Part 5: Lambda & Built-in Functions ⚡

### Lambda Functions (Anonymous one-line functions)
```python
add = lambda x, y: x + y  # Simple function
print(add(3, 4))  # Output: 7
```

### Built-in Functions (Predefined functions always available)

```python
len("Hello")        # Returns length → 5
type(10)            # Returns data type → <class 'int'>
int("5")            # Converts to integer → 5
str(10)             # Converts to string → "10"
float(5)            # Converts to float → 5.0
input("Enter name: ")  # Gets user input
sum([1, 2, 3])      # Sums values → 6
max([10, 3, 8])     # Finds maximum value → 10
min([10, 3, 8])     # Finds minimum value → 3
abs(-5)             # Absolute value → 5
round(3.14159, 2)   # Rounds number → 3.14
```

### Range Function (Generates sequence of numbers)
```python
range(5)           # Generates 0, 1, 2, 3, 4
range(2, 6)        # Generates 2, 3, 4, 5
range(1, 10, 2)    # Generates 1, 3, 5, 7, 9 (step 2)
```

---

## Part 6: Exception Handling 🛡️

Exception handling prevents program crashes from errors.

### Try-Except Block (Catch and handle errors)
```python
try:
    number = int(input("Enter a number: "))
    result = 10 / number
    print(f"Result: {result}")
except ValueError:
    print("That's not a valid number!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
except Exception as e:
    print(f"An error occurred: {e}")
else:
    print("Operation successful!")  # Runs if no error
finally:
    print("This always runs")  # Always executes
```

---

## Part 7: Data Structures Overview 📦

| Structure | Ordered | Mutable | Duplicates | Example |
|-----------|---------|---------|------------|---------|
| List | ✅ | ✅ | ✅ | `fruits = ["apple", "banana"]` |
| Tuple | ✅ | ❌ | ✅ | `coords = (10.5, 20.7)` |
| Set | ❌ | ✅ | ❌ | `colors = {"red", "green"}` |
| Dictionary | ✅ (Python 3.7+) | ✅ | Keys: ❌ | `person = {"name": "Alice"}` |

---

## Part 8: Lists & Methods 📋

Lists are ordered, changeable collections that allow duplicates.

### List Methods
```python
my_list = [1, 2, 3, 4]
my_list.append(5)          # Adds element at end → [1, 2, 3, 4, 5]
my_list.extend([6, 7])     # Adds multiple elements → [1, 2, 3, 4, 5, 6, 7]
my_list.insert(1, 99)      # Inserts at index 1 → [1, 99, 2, 3, 4, 5, 6, 7]
my_list.remove(3)          # Removes first matching value → [1, 99, 2, 4, 5, 6, 7]
item = my_list.pop()       # Removes and returns last item → 7
my_list.index(2)           # Returns index of value → 2
my_list.count(2)           # Counts occurrences → 1
my_list.sort()             # Sorts the list → [1, 2, 4, 5, 6, 99]
my_list.reverse()          # Reverses the list → [99, 6, 5, 4, 2, 1]
my_list.copy()             # Returns a copy of the list
my_list.clear()            # Removes all elements → []
```

### List Slicing (Access parts of a list)
```python
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
numbers[2:5]    # Elements from index 2 to 4 → [2, 3, 4]
numbers[:3]     # Elements from start to index 2 → [0, 1, 2]
numbers[5:]     # Elements from index 5 to end → [5, 6, 7, 8, 9]
numbers[::2]    # Every second element → [0, 2, 4, 6, 8]
numbers[::-1]   # Reverse the list → [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
```

---

## Part 9: Tuples 🎯

Tuples are ordered, unchangeable collections that allow duplicates.

### Tuple Operations
```python
my_tuple = (1, 2, 3)
len(my_tuple)              # Returns length → 3
my_tuple.index(2)          # Returns index of value → 1
my_tuple.count(1)          # Counts occurrences → 1
a, b, c = my_tuple         # Unpacking → a=1, b=2, c=3
t = (5,)                   # Single element (note comma)
```

### Tuple vs List
- Use tuples for data that shouldn't change (faster, safer)
- Use lists for data that needs to be modified

---

## Part 10: Sets 🔁

Sets are unordered, mutable collections of unique elements.

### Set Methods
```python
my_set = {1, 2, 3, 3}      # Duplicates removed → {1, 2, 3}
my_set.add(4)              # Adds element → {1, 2, 3, 4}
my_set.update([5, 6])      # Adds multiple elements → {1, 2, 3, 4, 5, 6}
my_set.remove(2)           # Removes element (raises error if not found)
my_set.discard(10)         # Removes element (no error if not found)
item = my_set.pop()        # Removes random element
my_set.clear()             # Removes all elements → set()
3 in my_set                # Membership check → True or False
```

### Set Operations
```python
a = {1, 2}; b = {2, 3}
a.union(b)                 # All elements from both sets → {1, 2, 3}
a | b                      # Union (same as above)
a.intersection(b)          # Common elements → {2}
a & b                      # Intersection (same as above)
a.difference(b)            # Elements in a not in b → {1}
a - b                      # Difference (same as above)
a.symmetric_difference(b)  # Elements in either set but not both → {1, 3}
a ^ b                      # Symmetric difference (same as above)
```

---

## Part 11: Dictionaries 📚

Dictionaries are unordered collections of key-value pairs (ordered in Python 3.7+).

### Dictionary Methods
```python
student = {"name": "Ravi", "age": 21}
student["name"]            # Access value → "Ravi"
student.get("grade", "N/A")  # Returns value or default → "N/A"
student.keys()             # All keys → dict_keys(['name', 'age'])
student.values()           # All values → dict_values(['Ravi', 21])
student.items()            # Key-value pairs → dict_items([('name', 'Ravi'), ('age', 21)])
student.update({"grade": "A"})  # Adds/updates pairs
student.pop("age")         # Removes key and returns value → 21
student.popitem()          # Removes last inserted pair
student.clear()            # Removes all items → {}
"name" in student          # Checks if key exists → True
```

### Dictionary Comprehension
```python
squares = {x: x**2 for x in range(1, 6)}
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
```

---

## Part 12: Strings 🔤

Strings are sequences of characters enclosed in quotes.

### String Operations
```python
text = "Hello, Python!"
len(text)                   # Returns length → 14
text.lower()               # Converts to lowercase → 'hello, python!'
text.upper()               # Converts to uppercase → 'HELLO, PYTHON!'
"  Hello  ".strip()        # Removes whitespace → 'Hello'
text.replace("Python", "World")  # Replaces text → 'Hello, World!'
text.split(",")            # Splits into list → ['Hello', ' Python!']
"-".join(["a", "b", "c"])  # Joins list into string → 'a-b-c'
text.find("P")             # Returns index of substring → 7
text.index("P")            # Returns index (raises error if not found) → 7
text.startswith("Hello")   # Checks if starts with → True
text.endswith("!")         # Checks if ends with → True
"123".isdigit()            # Checks if all characters are digits → True
"abc".isalpha()            # Checks if all characters are letters → True
f"Hello, {name}!"          # f-string formatting
text[7:13]                 # Slicing → 'Python'
```

### Escape Characters
```python
print("Line 1\nLine 2")    # New line → Line 1 (new line) Line 2
print("He said, \"Hello\"") # Quotes → He said, "Hello"
print("Path: C:\\folder")  # Backslash → Path: C:\folder
```

---

## Part 13: Important Keywords 🧠

Python keywords are reserved words with special meanings.

### 25 Common Python Keywords
1. `if` - Conditional execution
2. `else` - Alternate execution path
3. `elif` - Else if (multiple conditions)
4. `for` - Loop through sequences
5. `while` - Loop while condition is true
6. `break` - Exit loop immediately
7. `continue` - Skip to next iteration
8. `def` - Define a function
9. `return` - Return value from function
10. `import` - Import modules/packages
11. `from` - Import specific parts
12. `as` - Create alias for imports
13. `pass` - Placeholder (do nothing)
14. `in` - Check membership in sequence
15. `not` - Logical NOT operator
16. `and` - Logical AND operator
17. `or` - Logical OR operator
18. `is` - Identity comparison
19. `None` - Represents null/no value
20. `class` - Define a class
21. `try` - Begin exception handling block
22. `except` - Catch exceptions
23. `finally` - Always execute code
24. `raise` - Manually trigger exception
25. `lambda` - Create anonymous function

View all keywords:
```python
import keyword
print(keyword.kwlist)
```

---

## Part 14: List Comprehensions 🔁

List comprehensions provide a concise way to create lists.

### Basic Comprehension
```python
squares = [x**2 for x in range(5)]  # [0, 1, 4, 9, 16]
```

### With Condition
```python
even = [x for x in range(10) if x % 2 == 0]  # [0, 2, 4, 6, 8]
```

### Nested Loops
```python
pairs = [(x, y) for x in [1, 2] for y in [3, 4]]
# [(1, 3), (1, 4), (2, 3), (2, 4)]
```

### If-Else in Comprehension
```python
labels = ['Even' if x % 2 == 0 else 'Odd' for x in range(5)]
# ['Even', 'Odd', 'Even', 'Odd', 'Even']
```

### Set Comprehension
```python
unique = {x for x in [1, 2, 2, 3]}  # {1, 2, 3}
```

### Dictionary Comprehension
```python
squares = {x: x**2 for x in range(4)}  # {0: 0, 1: 1, 2: 4, 3: 9}
```

### Looping with enumerate() (Get index and value)
```python
for index, value in enumerate(['a', 'b']):
    print(index, value)  # 0 a, 1 b
```

### Looping with zip() (Iterate multiple sequences together)
```python
names = ['Ram', 'Shyam']
scores = [85, 90]
for name, score in zip(names, scores):
    print(name, score)  # Ram 85, Shyam 90
```

---

## Part 15-17: OOP Basics 🧱

Object-Oriented Programming (OOP) organizes code using classes and objects.

### Classes & Objects
A class is a blueprint, and an object is an instance of a class.

```python
class Car:
    # Constructor (initializes object)
    def __init__(self, brand, model):
        self.brand = brand  # Instance variable
        self.model = model
        
    # Method (function inside class)
    def drive(self):
        print(f"{self.brand} is driving")

# Create object (instance of class)
my_car = Car("Toyota", "Camry")
print(my_car.brand)  # Access attribute → Toyota
my_car.drive()       # Call method → Toyota is driving
```

### Class Variables (Shared across all instances)
```python
class Dog:
    species = "Canine"  # Class variable (shared)
    
    def __init__(self, name):
        self.name = name  # Instance variable (unique to each object)

print(Dog.species)  # Access class variable → Canine
d = Dog("Rocky")
print(d.species)    → Canine
print(d.name)       → Rocky
```

### Inheritance (Create new class based on existing class)
```python
class Animal:  # Parent class
    def speak(self):
        print("Sound")

class Dog(Animal):  # Child class (inherits from Animal)
    def speak(self):  # Method overriding
        print("Bark")

d = Dog()
d.speak()  # Output: Bark (uses child's method)
```

### Encapsulation (Restrict access to data)
```python
class Bank:
    def __init__(self):
        self.__balance = 0  # Private variable (name mangling)
    
    def get_balance(self):  # Getter method
        return self.__balance
    
    def deposit(self, amount):  # Setter method
        if amount > 0:
            self.__balance += amount
```

### Polymorphism (Same interface, different implementation)
```python
class Cat:
    def speak(self): 
        print("Meow")

class Dog:
    def speak(self): 
        print("Bark")

# Both have speak() method but different implementations
animals = [Cat(), Dog()]
for animal in animals:
    animal.speak()  # Output: Meow, Bark
```

### Special Methods (Dunder methods)
```python
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    
    def __str__(self):  # String representation
        return f"{self.title} by {self.author}"
    
    def __len__(self):  # Custom length
        return 100

book = Book("Python Basics", "John Doe")
print(book)   # Uses __str__ → "Python Basics by John Doe"
print(len(book))  # Uses __len__ → 100
```

---

## Part 18: File Handling 📁

### Reading Files
```python
# Read entire file
with open("file.txt", "r") as file:
    content = file.read()
    print(content)

# Read line by line
with open("file.txt", "r") as file:
    for line in file:
        print(line.strip())  # strip() removes newline characters
```

### Writing Files
```python
# Write to file (overwrites existing content)
with open("file.txt", "w") as file:
    file.write("Hello, World!")

# Append to file (adds to existing content)
with open("file.txt", "a") as file:
    file.write("\nAppended text")
```

### File Modes
- `"r"` - Read (default)
- `"w"` - Write (overwrites)
- `"a"` - Append
- `"x"` - Create (fails if exists)
- `"b"` - Binary mode
- `"t"` - Text mode (default)
- `"+"` - Read and write

---

## Part 19: Modules and Packages 📦

### Importing Modules
```python
import math                     # Import entire module
print(math.sqrt(16))           # → 4.0

from math import sqrt, pi       # Import specific functions
print(sqrt(16))                # → 4.0

import math as m               # Import with alias
print(m.sqrt(16))              # → 4.0

from math import *             # Import all (not recommended)
```

### Creating Your Own Module
Create a file named `mymodule.py`:
```python
def greet(name):
    return f"Hello, {name}!"

PI = 3.14159
```

Use your module:
```python
import mymodule
print(mymodule.greet("Alice"))  # → Hello, Alice!
print(mymodule.PI)              # → 3.14159
```

### Packages (Collections of modules)
Create a folder structure:
```
mypackage/
    __init__.py
    module1.py
    module2.py
```

Import from package:
```python
from mypackage import module1
from mypackage.module2 import function_name
```

---

*Created By Shekher Saksham Shashi (AMPICS)*
