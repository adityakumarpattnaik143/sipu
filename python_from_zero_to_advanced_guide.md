# Python From Zero to Advanced

A complete study guide for learning Python from the very beginning to advanced topics. This document is written for people who want to **read, understand, practice, and write Python code** step by step.

---

## Table of Contents

1. [What Python Is](#what-python-is)
2. [How to Start](#how-to-start)
3. [Level 0: Basics and Fundamentals](#level-0-basics-and-fundamentals)
4. [Control Flow](#control-flow)
5. [Built-in Data Structures](#built-in-data-structures)
6. [Functions and Scope](#functions-and-scope)
7. [Comprehensions and Iteration](#comprehensions-and-iteration)
8. [Modules, Packages, and Virtual Environments](#modules-packages-and-virtual-environments)
9. [File Handling and Data Formats](#file-handling-and-data-formats)
10. [Error and Exception Handling](#error-and-exception-handling)
11. [Object-Oriented Programming](#object-oriented-programming)
12. [Advanced Python Concepts](#advanced-python-concepts)
13. [Concurrency, Parallelism, and Async](#concurrency-parallelism-and-async)
14. [Professional Ecosystem and Tooling](#professional-ecosystem-and-tooling)
15. [Problem Solving Roadmap](#problem-solving-roadmap)
16. [Practice Projects](#practice-projects)
17. [Quick Revision Sheet](#quick-revision-sheet)

---

## What Python Is

Python is a **high-level, interpreted, general-purpose programming language**. It is popular because it is:

- easy to read,
- easy to write,
- beginner-friendly,
- powerful for web development, data science, automation, AI, scripting, and app development.

### Why Python is beginner-friendly

Python uses simple syntax and indentation instead of brackets for blocks.

```python
if True:
    print("Hello, Python!")
```

### Python execution model

```text
Your code  ->  Python Interpreter  ->  Output
```

Python reads code line by line and executes it.

---

## How to Start

### 1. Install Python

Install Python from the official Python website or use a package manager depending on your operating system.

### 2. Choose an editor or IDE

Common choices:
- **VS Code**: lightweight, popular, flexible.
- **PyCharm**: powerful, Python-focused IDE.
- **Jupyter Notebook**: great for data science and experiments.

### 3. Use the REPL

REPL means **Read, Evaluate, Print, Loop**.

You can test small Python expressions directly:

```python
>>> 2 + 3
5
```

### 4. Run a script

Save code in a file like `main.py` and run:

```bash
python main.py
```

### Mental model

```text
Type code -> Save file -> Run interpreter -> See result -> Fix errors -> Repeat
```

---

## Level 0: Basics and Fundamentals

This is the foundation. Do not rush this part.

### 1. Syntax and Structure

Python cares about **indentation**.

```python
if 5 > 2:
    print("Five is greater")
```

The indented line belongs to the `if` block.

### Comments

Comments are ignored by Python.

```python
# This is a single-line comment
```

Multi-line comments are usually written with triple quotes:

```python
"""
This is often used as a docstring.
It can also act like a multi-line comment.
"""
```

### Statement execution

Python runs code from top to bottom unless control flow changes the path.

```python
print("A")
print("B")
print("C")
```

Output:

```text
A
B
C
```

---

### 2. Variables

A variable stores a value.

```python
name = "Aditya"
age = 20
```

#### Naming rules

- Use meaningful names.
- Use `snake_case` for variables.
- Do not start with a number.
- Do not use Python keywords.

Good:
```python
student_name = "Ravi"
```

Bad:
```python
1name = "Ravi"
class = "A"
```

#### Visualization

```text
name  ->  "Aditya"
age   ->  20
```

The variable name points to a value.

---

### 3. Primitive Data Types

#### int
Whole numbers.

```python
x = 10
```

#### float
Decimal numbers.

```python
y = 3.14
```

#### str
Text.

```python
message = "Hello"
```

#### bool
True or False.

```python
is_valid = True
```

#### None
Represents no value.

```python
result = None
```

### Type checking

```python
print(type(10))      # <class 'int'>
print(type(3.14))    # <class 'float'>
print(type("hi"))   # <class 'str'>
```

---

### 4. Type Conversion

Sometimes one type must be converted to another.

#### Implicit conversion
Python does it automatically.

```python
x = 5
y = 2.0
print(x + y)   # 7.0
```

#### Explicit conversion
You do it using functions.

```python
num = int("10")
pi = float("3.14")
text = str(100)
```

### Common conversion rules

```python
int("25")     # 25
float("12")   # 12.0
str(99)        # "99"
```

---

### 5. Basic Input and Output

#### print()
Used to display output.

```python
print("Hello")
```

You can control formatting:

```python
print("A", "B", sep="-")
print("Hello", end=" ")
print("World")
```

#### input()
Used to receive user input.

```python
name = input("Enter your name: ")
print("Welcome", name)
```

Important: `input()` always returns a string.

```python
age = int(input("Enter age: "))
```

---

### 6. Operators

#### Arithmetic

```python
+   # addition
-   # subtraction
*   # multiplication
/   # division
//  # floor division
%   # modulo
**  # power
```

Example:

```python
print(10 + 3)   # 13
print(10 / 3)   # 3.333...
print(10 // 3)  # 3
print(10 % 3)   # 1
print(2 ** 3)   # 8
```

#### Assignment

```python
x = 5
x += 2
x -= 1
x *= 3
```

#### Comparison

```python
==  # equal
!=  # not equal
<   # less than
>   # greater than
<=  # less than or equal
>=  # greater than or equal
```

#### Logical

```python
and
or
not
```

Example:

```python
age = 20
has_id = True
print(age >= 18 and has_id)
```

#### Identity

```python
is
is not
```

Used to check whether two variables point to the same object.

#### Membership

```python
in
not in
```

Example:

```python
print("a" in "banana")
```

#### Bitwise

Used on binary representations.

```python
&   # AND
|   # OR
^   # XOR
~   # NOT
<<  # left shift
>>  # right shift
```

### Operator visualization

```text
5 + 2 = 7
5 > 2 = True
"a" in "cat" = True
```

---

## Control Flow

Control flow decides which instructions run.

### 1. Conditionals

```python
age = 18
if age >= 18:
    print("Adult")
elif age >= 13:
    print("Teen")
else:
    print("Child")
```

### Flow chart

```text
Start -> Check condition -> True? -> Run block
                        -> False -> Next condition / else
```

---

### 2. Ternary Operator

A short form of `if-else`.

```python
result = "Pass" if marks >= 40 else "Fail"
```

---

### 3. Pattern Matching

Python 3.10+ supports `match` and `case`.

```python
command = "start"

match command:
    case "start":
        print("Starting")
    case "stop":
        print("Stopping")
    case _:
        print("Unknown command")
```

The underscore `_` means default case.

---

### 4. Loops

Loops repeat work.

#### for loop

```python
for i in range(5):
    print(i)
```

#### while loop

```python
count = 0
while count < 5:
    print(count)
    count += 1
```

### Loop control

#### break
Stops the loop.

```python
for i in range(10):
    if i == 5:
        break
    print(i)
```

#### continue
Skips the current iteration.

```python
for i in range(5):
    if i == 2:
        continue
    print(i)
```

#### pass
Does nothing.

```python
if True:
    pass
```

#### else with loops
The `else` block runs if the loop ends normally.

```python
for i in range(3):
    print(i)
else:
    print("Loop completed")
```

---

## Built-in Data Structures

Python has built-in containers for organizing data.

### 1. Strings (`str`)

Strings are **immutable**, meaning they cannot be changed in place.

```python
text = "Python"
```

#### Indexing

```python
text[0]   # 'P'
text[-1]  # 'n'
```

#### Slicing

```python
text[0:3]   # 'Pyt'
text[:3]    # 'Pyt'
text[2:]    # 'thon'
text[::2]   # 'Pto'
```

#### Formatting

##### f-strings

```python
name = "Ravi"
age = 21
print(f"Name: {name}, Age: {age}")
```

##### .format()

```python
print("Name: {}, Age: {}".format(name, age))
```

##### % formatting

```python
print("Name: %s, Age: %d" % (name, age))
```

#### Escape characters

```python
\n  # new line
\t  # tab
\\  # backslash
```

#### Common methods

```python
.upper()
.lower()
.split()
.join()
.strip()
.replace()
```

Example:

```python
sentence = "  hello world  "
print(sentence.strip().upper())
```

#### Visualization

```text
"Python"
 P  y  t  h  o  n
 0  1  2  3  4  5
-6 -5 -4 -3 -2 -1
```

---

### 2. Lists (`list`)

Lists are **mutable**, ordered collections.

```python
numbers = [1, 2, 3]
```

They can hold mixed types.

```python
items = [1, "hello", 3.5, True]
```

#### Indexing and slicing

```python
items[0]
items[1:3]
```

#### Common methods

```python
.append()
.extend()
.insert()
.remove()
.pop()
.sort()
.reverse()
.index()
.count()
```

Example:

```python
nums = [3, 1, 2]
nums.sort()
print(nums)  # [1, 2, 3]
```

#### Visualization

```text
[10, 20, 30]
 0   1   2
```

---

### 3. Tuples (`tuple`)

Tuples are **immutable** and ordered.

```python
point = (10, 20)
```

#### Packing and unpacking

```python
a, b = (1, 2)
```

#### Single-element tuple

```python
one = (5,)
```

The comma is necessary.

---

### 4. Dictionaries (`dict`)

Dictionaries store **key-value pairs**.

```python
student = {"name": "Ravi", "age": 20}
```

Keys must be immutable types like strings, numbers, or tuples.

#### Accessing values

```python
student["name"]
student.get("age")
```

#### Methods

```python
.keys()
.values()
.items()
.get()
.update()
.pop()
```

#### Visualization

```text
{
  "name" -> "Ravi",
  "age"  -> 20
}
```

---

### 5. Sets (`set`)

Sets store **unique** elements.

```python
fruits = {"apple", "banana", "mango"}
```

#### Properties

- unordered,
- mutable,
- no duplicates.

#### Set operations

```python
.union()
.intersection()
.difference()
.symmetric_difference()
```

Example:

```python
a = {1, 2, 3}
b = {3, 4, 5}
print(a.union(b))
```

---

## Functions and Scope

Functions help you reuse code.

### 1. Define a function

```python
def greet():
    print("Hello")
```

### 2. Call a function

```python
greet()
```

### 3. Parameters and arguments

```python
def add(a, b):
    return a + b
```

Types of arguments:

- positional arguments,
- keyword arguments,
- default arguments.

```python
def power(base, exp=2):
    return base ** exp
```

### 4. Flexible arguments

#### *args
Stores extra positional arguments as a tuple.

```python
def total(*args):
    return sum(args)
```

#### **kwargs
Stores extra keyword arguments as a dictionary.

```python
def show_info(**kwargs):
    print(kwargs)
```

### 5. Return values

```python
def square(x):
    return x * x
```

A function can return multiple values as a tuple:

```python
def stats():
    return 10, 20
```

### 6. Scope and namespace

Python follows the **LEGB rule**:

```text
L -> Local
E -> Enclosing
G -> Global
B -> Built-in
```

#### global

```python
count = 0

def change():
    global count
    count += 1
```

#### nonlocal

Used in nested functions.

```python
def outer():
    x = 10
    def inner():
        nonlocal x
        x += 1
```

### 7. Lambda functions

Small anonymous functions.

```python
square = lambda x: x * x
```

### 8. Higher-order functions

Functions that take other functions.

```python
map()
filter()
reduce()
```

Example:

```python
nums = [1, 2, 3]
print(list(map(lambda x: x * 2, nums)))
```

### 9. Docstrings

Use docstrings to explain a function.

```python
def add(a, b):
    """Return the sum of two numbers."""
    return a + b
```

---

## Comprehensions and Iteration

Comprehensions are a short way to build collections.

### 1. List comprehension

```python
squares = [x * x for x in range(5)]
```

### 2. Dictionary comprehension

```python
square_map = {x: x * x for x in range(5)}
```

### 3. Set comprehension

```python
unique_lengths = {len(word) for word in ["cat", "dog", "lion"]}
```

### 4. Generator expression

```python
gen = (x * x for x in range(5))
```

### 5. Useful iteration tools

```python
zip()
enumerate()
reversed()
sorted()
```

Example:

```python
names = ["A", "B"]
marks = [90, 95]
for i, (name, mark) in enumerate(zip(names, marks)):
    print(i, name, mark)
```

---

## Modules, Packages, and Virtual Environments

### 1. Modules

A module is a Python file.

```python
import math
from math import sqrt
import math as m
```

### 2. Standard library

Useful modules:

- `math` for mathematics,
- `random` for random numbers,
- `datetime` for dates and times,
- `os` for operating system features,
- `sys` for system-specific values,
- `re` for regular expressions,
- `json` for JSON handling.

### 3. Custom modules

Create your own file like `helper.py` and import it.

### 4. Packages

A package is a directory of modules.

```text
my_package/
    __init__.py
    module1.py
    module2.py
```

### 5. Main guard

```python
if __name__ == "__main__":
    print("This file is running directly")
```

### 6. Environment management

#### pip
Install packages.

```bash
pip install requests
```

#### venv
Create isolated environments.

```bash
python -m venv env
```

#### requirements.txt
List project dependencies.

```text
requests
pandas
numpy
```

---

## File Handling and Data Formats

### 1. Basic file operations

```python
file = open("data.txt", "r")
content = file.read()
file.close()
```

### 2. Better way: with statement

```python
with open("data.txt", "r") as file:
    content = file.read()
```

### 3. File modes

- `r` = read
- `w` = write
- `a` = append
- `r+` = read and write
- `rb`, `wb` = binary modes

### 4. Common file methods

```python
.read()
.readline()
.readlines()
.write()
.writelines()
```

### 5. JSON

```python
import json

with open("data.json", "r") as f:
    data = json.load(f)
```

To save JSON:

```python
with open("data.json", "w") as f:
    json.dump(data, f, indent=4)
```

### 6. CSV

```python
import csv

with open("data.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
```

---

## Error and Exception Handling

Errors happen. Good programs handle them properly.

### 1. Syntax errors vs exceptions

- **Syntax error**: code is written incorrectly.
- **Exception**: error occurs while program runs.

### 2. try / except / else / finally

```python
try:
    num = int(input("Enter a number: "))
except ValueError:
    print("Invalid number")
else:
    print("You entered", num)
finally:
    print("Program finished")
```

### 3. Specific exceptions

```python
except ValueError:
    print("Wrong input")
except Exception as e:
    print("Something went wrong:", e)
```

### 4. Raising exceptions

```python
raise Exception("Error message")
```

### 5. Custom exceptions

```python
class MyError(Exception):
    pass
```

### 6. Assertions

```python
assert x > 0, "x must be positive"
```

---

## Object-Oriented Programming

OOP organizes code using **classes** and **objects**.

### 1. Class and object

```python
class Car:
    pass

my_car = Car()
```

### 2. Constructor

```python
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
```

### 3. Methods

```python
class Car:
    def drive(self):
        print("Driving")
```

### 4. Instance variables and class variables

```python
class Student:
    school = "ABC School"   # class variable

    def __init__(self, name):
        self.name = name       # instance variable
```

### 5. Encapsulation

Use `_var` for protected-style naming and `__var` for name-mangled private-style naming.

```python
class A:
    def __init__(self):
        self._x = 1
        self.__y = 2
```

### 6. Property decorator

```python
class Person:
    def __init__(self, age):
        self._age = age

    @property
    def age(self):
        return self._age
```

### 7. Inheritance

A child class can reuse a parent class.

```python
class Animal:
    def speak(self):
        print("Animal sound")

class Dog(Animal):
    def speak(self):
        print("Bark")
```

Types of inheritance:

- single,
- multiple,
- multilevel.

### 8. super()

```python
class Parent:
    def __init__(self):
        print("Parent")

class Child(Parent):
    def __init__(self):
        super().__init__()
        print("Child")
```

### 9. Polymorphism

Different objects can respond differently to the same method.

```python
class Cat:
    def speak(self):
        print("Meow")
```

### 10. Dunder methods

Special methods used by Python.

```python
__str__
__repr__
__len__
__add__
__eq__
```

Example:

```python
class Box:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"Box({self.value})"
```

### 11. Abstract Base Classes

Used when you want to force child classes to implement methods.

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
```

---

## Advanced Python Concepts

### 1. Iterators

An iterator is an object that remembers where it is in a sequence.

```python
nums = iter([1, 2, 3])
print(next(nums))
```

Important terms:

- `__iter__()`
- `__next__()`
- `StopIteration`

### Iterator flow

```text
Iterable -> iterator -> next item -> next item -> StopIteration
```

### 2. Generators

Generators produce values one by one using `yield`.

```python
def count_up_to(n):
    i = 1
    while i <= n:
        yield i
        i += 1
```

Advantages:

- memory efficient,
- great for large data,
- lazy evaluation.

### 3. Decorators

Decorators modify the behavior of functions.

```python
def my_decorator(func):
    def wrapper():
        print("Before")
        func()
        print("After")
    return wrapper
```

### 4. Context managers

Used for resource handling.

```python
with open("file.txt") as f:
    data = f.read()
```

Custom context managers can be created with `__enter__` and `__exit__`, or with `contextlib.contextmanager`.

### 5. Type hinting

Type hints improve readability and help tools.

```python
def greet(name: str) -> str:
    return "Hello " + name
```

Common typing tools:

- `List`
- `Dict`
- `Optional`
- `Union`
- `Any`
- `Callable`

### 6. Memory management

Python manages memory using reference counting and garbage collection.

You should understand:

- references,
- objects,
- shallow copy vs deep copy.

```python
import copy
new_list = copy.copy(old_list)
deep_list = copy.deepcopy(old_list)
```

### 7. Regular expressions

Used for text pattern matching.

```python
import re
re.search()
re.match()
re.findall()
re.sub()
```

Example:

```python
import re
text = "My number is 12345"
print(re.findall(r"\d+", text))
```

---

## Concurrency, Parallelism, and Async

### 1. GIL

The Global Interpreter Lock is a Python mechanism that affects CPU-bound threading in standard CPython.

### 2. Threading

Threads are useful for I/O-bound tasks.

```python
import threading
```

Thread pool example:

```python
from concurrent.futures import ThreadPoolExecutor
```

### 3. Multiprocessing

Use multiple processes for CPU-heavy work.

```python
from multiprocessing import Process
from concurrent.futures import ProcessPoolExecutor
```

### 4. Async programming

Useful for many waiting tasks like network requests.

```python
import asyncio

async def main():
    await asyncio.sleep(1)
```

### Async visualization

```text
Task 1 ----wait---->
Task 2 ---wait----->
Task 3 ----wait---->
Event loop switches between them
```

---

## Professional Ecosystem and Tooling

### 1. Advanced data structures

From `collections`:

- `Counter`
- `defaultdict`
- `namedtuple`
- `deque`

Also:

- `heapq`

### 2. Testing

Testing ensures your code works.

```python
import unittest
```

Also popular:

- `pytest`
- `unittest.mock`
- TDD = Test-Driven Development

### 3. Debugging

Use:

- `pdb`,
- IDE breakpoints,
- print debugging when learning.

### 4. Logging

```python
import logging
logging.basicConfig(level=logging.INFO)
```

Levels:

- DEBUG
- INFO
- WARNING
- ERROR
- CRITICAL

### 5. Network requests

Use `urllib` or `requests`.

Common HTTP methods:

- GET
- POST
- PUT
- DELETE

Example:

```python
import requests
response = requests.get("https://example.com")
print(response.status_code)
```

---

## Problem Solving Roadmap

### Beginner path

1. Learn syntax.
2. Practice variables and types.
3. Use `if`, loops, and functions.
4. Work with lists, tuples, dicts, and sets.
5. Solve small problems daily.

### Intermediate path

1. Understand modules.
2. Learn file handling.
3. Handle exceptions.
4. Build classes and objects.
5. Use comprehensions and generators.

### Advanced path

1. Learn decorators and iterators.
2. Study async and concurrency.
3. Use testing and logging.
4. Learn packaging and environments.
5. Build real projects.

### Learning cycle

```text
Learn -> Practice -> Make mistakes -> Debug -> Improve -> Repeat
```

---

## Practice Projects

Start with small projects and grow gradually.

### Beginner projects

- calculator,
- number guessing game,
- to-do list in terminal,
- basic quiz app,
- simple file reader.

### Intermediate projects

- student management system,
- contact book,
- expense tracker,
- weather app using API,
- text analyzer.

### Advanced projects

- Flask or Django web app,
- automation bot,
- data analysis pipeline,
- REST API client,
- multithreaded downloader.

### Project progression diagram

```text
Hello World
   -> Calculator
   -> Quiz Game
   -> File Manager
   -> API App
   -> OOP Project
   -> Full Web App
   -> Advanced System
```

---

## Quick Revision Sheet

### Core basics

- variables store data,
- types define data kind,
- operators perform actions,
- input takes data from user,
- print shows output.

### Control flow

- `if`, `elif`, `else`
- `for`, `while`
- `break`, `continue`, `pass`

### Data structures

- `list` = mutable sequence
- `tuple` = immutable sequence
- `dict` = key-value map
- `set` = unique elements
- `str` = immutable text

### Functions

- `def`
- `return`
- `*args`
- `**kwargs`
- scope
- lambda

### Advanced

- iterators
- generators
- decorators
- context managers
- type hints
- exceptions
- OOP
- async
- testing
- logging

---

## Final Study Advice

To become strong in Python:

1. read the concept,
2. type the examples yourself,
3. change the code and observe output,
4. solve exercises without looking,
5. build small projects.

Python becomes easy when you practice daily.

---

## Mini Cheat Visuals

### Variable and value

```text
x  ->  10
name -> "Python"
```

### Function

```text
input -> function -> output
```

### List

```text
[1, 2, 3, 4]
 0  1  2  3
```

### Dictionary

```text
key ----> value
```

### Loop

```text
start -> repeat -> repeat -> stop
```

### Generator

```text
produce one value -> pause -> produce next value
```

---

## End

This guide is meant to be a complete starting map for Python learning. Practice each topic with code examples, then build projects to make the ideas permanent.

