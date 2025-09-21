# Python Basics Cheat Sheet 🐍📚

## Part 1: Data Types & Variables

### What is a Variable?
A variable stores data in memory to be used and modified later.

```python
name = "Alice"
age = 25
```

### Common Python Data Types

| Type | Description | Example |
|------|-------------|---------|
| `str` | Text data | `message = "Hello, World"` |
| `int` | Whole numbers | `count = 42` |
| `float` | Decimal numbers | `price = 19.99` |
| `bool` | True or False | `is_valid = True` |
| `list` | Ordered, mutable sequence | `fruits = ["apple", "banana", "cherry"]` |
| `tuple` | Ordered, immutable sequence | `coords = (10.5, 20.7)` |
| `set` | Unordered collection of unique elements | `colors = {"red", "green", "blue"}` |
| `dict` | Key-value pairs | `person = {"name": "Alice", "age": 25}` |

**Dynamic Typing**: Python automatically detects the type.

---

## Part 2: Operators in Python ⚙️

### Arithmetic Operators
```python
a = 10; b = 3
a + b   # Addition → 13
a - b   # Subtraction → 7
a * b   # Multiplication → 30
a / b   # Division → 3.33
a % b   # Modulus → 1
a ** b  # Exponent → 1000
a // b  # Floor Division → 3
```

### Comparison Operators
```python
a == b  # Equal
a != b  # Not equal
a > b   # Greater than
a < b   # Less than
a >= b  # Greater than or equal
a <= b  # Less than or equal
```

### Logical Operators
```python
x = True; y = False
x and y  # False
x or y   # True
not x    # False
```

### Assignment Operators
```python
x = 5
x += 3  # x = x + 3 → 8
x -= 2  # x = x - 2 → 6
```

---

## Part 3: Control Flow 🔁

### Conditional Statements
```python
age = 18
if age >= 18:
    print("You are an adult")
elif age > 13:
    print("You are a teenager")
else:
    print("You are a child")
```

### Loops
**For Loop:**
```python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
```

**While Loop:**
```python
count = 0
while count < 5:
    print(count)
    count += 1
```

### Loop Control Statements
- `break`: Exit the loop
- `continue`: Skip current iteration
- `pass`: Placeholder that does nothing

```python
for i in range(5):
    if i == 3:
        break
    print(i)
```

---

## Part 4: Functions 🧩

### Defining a Function
```python
def greet(name):
    print(f"Hello, {name}!")
```

### Calling a Function
```python
greet("Alice")
```

### Return Statement
```python
def add(a, b):
    return a + b

result = add(3, 5)  # Output: 8
```

### Default Parameters
```python
def greet(name="Guest"):
    print(f"Hello, {name}")
```

### Keyword Arguments
```python
def info(name, age):
    print(f"{name} is {age} years old")

info(age=25, name="Bob")
```

### Variable-Length Arguments
```python
def show_args(*args):
    print(args)

def show_kwargs(**kwargs):
    print(kwargs)
```

---

## Part 5: Lambda & Built-in Functions ⚡

### Lambda Functions
```python
add = lambda x, y: x + y
print(add(3, 4))  # Output: 7
```

### Built-in Functions
```python
len("Hello")        # 5
type(10)            # <class 'int'>
int("5")            # 5
input("Enter name: ")
sum([1, 2, 3])      # 6
max([10, 3, 8])     # 10
```

---

## Part 7: Data Structures Overview 📦

| Structure | Ordered | Mutable | Duplicates | Example |
|-----------|---------|---------|------------|---------|
| List | ✅ | ✅ | ✅ | `fruits = ["apple", "banana"]` |
| Tuple | ✅ | ❌ | ✅ | `coords = (10.5, 20.7)` |
| Set | ❌ | ✅ | ❌ | `colors = {"red", "green"}` |
| Dictionary | ❌ | ✅ | Keys: ❌ | `person = {"name": "Alice"}` |

---

## Part 8: Lists & Methods 📋

### List Methods
```python
my_list = [1, 2, 3, 4]
my_list.append(5)          # Adds element at end
my_list.extend([6, 7])     # Adds multiple elements
my_list.insert(1, 99)      # Inserts at index 1
my_list.remove(3)          # Removes first matching value
item = my_list.pop()       # Removes and returns last item
my_list.index(2)           # Returns index of value
my_list.count(2)           # Counts occurrences
my_list.sort()             # Sorts the list
my_list.reverse()          # Reverses the list
my_list.clear()            # Removes all elements
```

---

## Part 9: Tuples 🎯

### Tuple Operations
```python
my_tuple = (1, 2, 3)
len(my_tuple)              # 3
my_tuple.index(2)          # 1
my_tuple.count(1)          # 1
a, b, c = my_tuple         # Unpacking
t = (5,)                   # Single element (note comma)
```

---

## Part 10: Sets 🔁

### Set Methods
```python
my_set = {1, 2, 3, 3}      # {1, 2, 3}
my_set.add(4)
my_set.update([5, 6])
my_set.remove(2)           # Raises error if not found
my_set.discard(10)         # No error if not found
item = my_set.pop()        # Removes random element
my_set.clear()
3 in my_set                # Membership check
```

### Set Operations
```python
a = {1, 2}; b = {2, 3}
a.union(b)                 # {1, 2, 3}
a.intersection(b)          # {2}
a.difference(b)            # {1}
```

---

## Part 11: Dictionaries 📚

### Dictionary Methods
```python
student = {"name": "Ravi", "age": 21}
student.get("grade", "N/A")  # Returns value or default
student.keys()              # All keys
student.values()            # All values
student.items()             # Key-value pairs
student.update({"grade": "A"})  # Adds/updates pairs
student.pop("age")          # Removes key and returns value
student.popitem()           # Removes last inserted pair
student.clear()             # Removes all items
"name" in student           # True
```

---

## Part 12: Strings 🔤

### String Operations
```python
text = "Hello, Python!"
len(text)                   # 14
text.lower()               # 'hello, python!'
text.upper()               # 'HELLO, PYTHON!'
"  Hello  ".strip()        # 'Hello'
text.replace("Python", "World")  # 'Hello, World!'
text.split(",")            # ['Hello', ' Python!']
"-".join(["a", "b", "c"])  # 'a-b-c'
text.find("P")             # 7
text.index("P")            # 7
text.startswith("Hello")   # True
text.endswith("!")         # True
"123".isdigit()            # True
"abc".isalpha()            # True
f"Hello, {name}!"          # Formatting
```

---

## Part 13: Important Keywords 🧠

### 25 Common Python Keywords
1. `if` - Conditional logic
2. `else` - Alternate block
3. `elif` - Else if
4. `for` - Loop through sequence
5. `while` - Loop while condition true
6. `break` - Exit loop
7. `continue` - Skip iteration
8. `def` - Define function
9. `return` - Return value
10. `import` - Import modules
11. `from` - Import specific parts
12. `as` - Rename imported module
13. `pass` - Do nothing
14. `in` - Check presence
15. `not` - Logical NOT
16. `and` - Logical AND
17. `or` - Logical OR
18. `is` - Identity check
19. `None` - Null object
20. `class` - Define class
21. `try` - Error-handling block
22. `except` - Catch errors
23. `finally` - Always executes
24. `raise` - Manually raise error
25. `lambda` - Anonymous function

View all keywords:
```python
import keyword
print(keyword.kwlist)
```

---

## Part 14: List Comprehensions 🔁

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

### Looping with enumerate()
```python
for index, value in enumerate(['a', 'b']):
    print(index, value)
```

### Looping with zip()
```python
names = ['Ram', 'Shyam']
scores = [85, 90]
for name, score in zip(names, scores):
    print(name, score)
```

---

## Part 15-17: OOP Basics 🧱

### Classes & Objects
```python
class Car:
    def __init__(self, brand, model):
        self.brand = brand  # Instance variable
        self.model = model
        
    def drive(self):  # Method
        print(f"{self.brand} is driving")

my_car = Car("Toyota", "Camry")
print(my_car.brand)  # Toyota
my_car.drive()       # Toyota is driving
```

### Class Variables
```python
class Dog:
    species = "Canine"  # Class variable
    
    def __init__(self, name):
        self.name = name  # Instance variable

print(Dog.species)  # Canine
d = Dog("Rocky")
print(d.species)    # Canine
```

### Inheritance
```python
class Animal:
    def speak(self):
        print("Sound")

class Dog(Animal):  # Inherits from Animal
    pass

d = Dog()
d.speak()  # Output: Sound
```

### Encapsulation
```python
class Bank:
    def __init__(self):
        self.__balance = 0  # Private variable
```

### Polymorphism
```python
class Cat:
    def speak(self): 
        print("Meow")

class Dog:
    def speak(self): 
        print("Bark")
```

---

*Created By Shekher Saksham Shashi (AMPICS)*
