# Python Learning Guide
**Curated by ADITYA KUMAR PATTNAIK**

Welcome to your Python learning journey! This guide is designed to take you from a complete beginner (zero) to an advanced Python programmer. It provides step-by-step instructions, clear definitions, examples, and sample test cases.

---

## Basic Knowledge Transfer (KT): Working with this Repository

Before diving into Python, here is how you will write code and test it on your local machine.

### 1. Repository Structure
All your daily code practice should be stored in the `daily_codes/` directory of this repository.

### 2. Writing Python Code
- Create a Python file for the concept you are learning. For example, `daily_codes/variables.py`.
- Write your code inside this file using functions so it can be tested easily.

### 3. Writing Test Cases
- We use a testing tool called `pytest` to verify our code works.
- For every Python file you create, you should create a corresponding test file in the *same directory* (`daily_codes/`).
- The test file name **must** start with `test_`. For example, `test_variables.py`.

### 4. Example KT Workflow
**Create your code file (`daily_codes/hello.py`):**
```python
# daily_codes/hello.py
def say_hello(name):
    return f"Hello, {name}!"
```

**Create your test file (`daily_codes/test_hello.py`):**
```python
# daily_codes/test_hello.py
from hello import say_hello

def test_say_hello():
    assert say_hello("Aditya") == "Hello, Aditya!"
```

**Running your tests:**
Open your terminal, navigate to the repository root, and run:
```bash
pytest daily_codes/
```

---

## Part 1: Python Basics

### 1. Variables and Data Types
**Definition:** Variables are containers for storing data values. Python has various data types like Integers (`int`), Floats (`float`), Strings (`str`), and Booleans (`bool`).

**Example Code (`daily_codes/basics.py`):**
```python
def add_numbers(a, b):
    return a + b

def greet_user(name):
    return "Welcome, " + name
```

**Test Case (`daily_codes/test_basics.py`):**
```python
from basics import add_numbers, greet_user

def test_add_numbers():
    assert add_numbers(5, 3) == 8 # Output should be 8

def test_greet_user():
    assert greet_user("Brother") == "Welcome, Brother" # Output should be "Welcome, Brother"
```

### 2. Control Flow (If/Else Statements)
**Definition:** Control flow allows your program to make decisions and execute different code blocks based on conditions.

**Example Code (`daily_codes/control_flow.py`):**
```python
def check_even_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"
```

**Test Case (`daily_codes/test_control_flow.py`):**
```python
from control_flow import check_even_odd

def test_check_even_odd():
    assert check_even_odd(4) == "Even"
    assert check_even_odd(7) == "Odd"
```

### 3. Loops (For and While)
**Definition:** Loops are used for iterating over a sequence (like a list, tuple, dictionary, set, or string) or repeating an action while a condition is true.

**Example Code (`daily_codes/loops.py`):**
```python
def sum_of_list(numbers):
    total = 0
    for num in numbers:
        total += num
    return total
```

**Test Case (`daily_codes/test_loops.py`):**
```python
from loops import sum_of_list

def test_sum_of_list():
    assert sum_of_list([1, 2, 3, 4]) == 10
```

---

## Part 2: Intermediate Python

### 4. Lists, Dictionaries, and Sets
**Definition:**
- **Lists:** Ordered, mutable collections of items.
- **Dictionaries:** Key-value pairs.
- **Sets:** Unordered collections of unique items.

**Example Code (`daily_codes/data_structures.py`):**
```python
def get_user_age(user_dict, name):
    # Returns age if user exists, else returns "Not Found"
    return user_dict.get(name, "Not Found")

def get_unique_items(item_list):
    # Converts list to set to remove duplicates, then back to list
    return list(set(item_list))
```

**Test Case (`daily_codes/test_data_structures.py`):**
```python
from data_structures import get_user_age, get_unique_items

def test_get_user_age():
    users = {"Aditya": 25, "Brother": 20}
    assert get_user_age(users, "Brother") == 20
    assert get_user_age(users, "Unknown") == "Not Found"

def test_get_unique_items():
    assert sorted(get_unique_items([1, 2, 2, 3, 3, 4])) == [1, 2, 3, 4]
```

### 5. Exception Handling
**Definition:** Handling runtime errors smoothly using `try`, `except`, `finally` blocks so your program doesn't crash.

**Example Code (`daily_codes/exceptions.py`):**
```python
def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Cannot divide by zero!"
```

**Test Case (`daily_codes/test_exceptions.py`):**
```python
from exceptions import safe_divide

def test_safe_divide():
    assert safe_divide(10, 2) == 5.0
    assert safe_divide(10, 0) == "Cannot divide by zero!"
```

---

## Part 3: Advanced Python

### 6. Object-Oriented Programming (OOP)
**Definition:** A programming paradigm based on the concept of "objects", which can contain data and code (attributes and methods).

**Example Code (`daily_codes/oop.py`):**
```python
class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        return f"{self.name} says Woof!"
```

**Test Case (`daily_codes/test_oop.py`):**
```python
from oop import Dog

def test_dog_bark():
    my_dog = Dog("Buddy")
    assert my_dog.bark() == "Buddy says Woof!"
```

### 7. File Handling
**Definition:** Reading from and writing to files on your system.

**Example Code (`daily_codes/file_ops.py`):**
```python
import os

def write_and_read_file(filename, content):
    # Write to file
    with open(filename, 'w') as f:
        f.write(content)

    # Read from file
    with open(filename, 'r') as f:
        read_content = f.read()

    # Clean up (delete file after reading)
    if os.path.exists(filename):
        os.remove(filename)

    return read_content
```

**Test Case (`daily_codes/test_file_ops.py`):**
```python
from file_ops import write_and_read_file

def test_write_and_read_file():
    content = "Learning Python is fun!"
    filename = "test_temp.txt"
    assert write_and_read_file(filename, content) == content
```

### 8. List Comprehensions and Generators
**Definition:** Concise ways to create lists and iterators.

**Example Code (`daily_codes/advanced_iterables.py`):**
```python
def get_squares(numbers):
    # List comprehension
    return [x * x for x in numbers]
```

**Test Case (`daily_codes/test_advanced_iterables.py`):**
```python
from advanced_iterables import get_squares

def test_get_squares():
    assert get_squares([1, 2, 3, 4]) == [1, 4, 9, 16]
```

---
*Happy Coding! Start by creating your first file in the `daily_codes/` folder today!*
