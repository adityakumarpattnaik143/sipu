# Comprehensive Python Learning Guide
**Curated by ADITYA KUMAR PATTNAIK**

Welcome to the ultimate Python learning journey! This guide takes you from absolute beginner (Level 0) to advanced professional. It includes detailed theory, practical examples, and test cases for each topic.

---

## Basic Knowledge Transfer (KT) & Setup

### Environment Setup: Running Python on Your Local Machine
1. **Install Python:** Go to [python.org/downloads](https://www.python.org/downloads/) and install the latest version. **Windows Users:** Check the box "Add Python to PATH" during installation.
2. **Verify Installation:** Open a terminal and run `python --version` (or `python3 --version`).
3. **IDE:** Download **Visual Studio Code (VS Code)** and install the "Python" extension.

### Repository Workflow & Testing
All your code should go inside the `daily_codes/` directory.

1. **Write Code:** Create a file like `daily_codes/hello.py`.
2. **Write Tests:** Create a test file like `daily_codes/test_hello.py` to test your functions.
3. **Run Code:** Use `python daily_codes/hello.py`.
4. **Run Tests:** We use `pytest`. Install it using `pip install pytest`, then run:
   ```bash
   pytest daily_codes/
   ```

---

## 1. Basics & Fundamentals (Level 0)

### Theory
- **Syntax & Structure:** Python uses indentation (spaces/tabs) instead of `{}`.
- **Comments:** Use `#` for single-line and `"""` for multi-line.
- **Variables:** Storing data (e.g., `x = 5`). Use `snake_case` for naming.
- **Types:** `int`, `float`, `str`, `bool`, `None`. Use `type(x)` to check.
- **Type Casting:** `int("5")` converts string to integer.
- **I/O:** `print()` for output, `input()` for taking user input.
- **Operators:** Arithmetic (`+`, `-`, `*`, `/`, `//`, `%`, `**`), Comparison (`==`, `!=`), Logical (`and`, `or`, `not`).

### Example (`daily_codes/fundamentals.py`)
```python
def check_type_and_math(val1_str, val2_int):
    val1_int = int(val1_str) # Explicit casting
    return val1_int ** val2_int # Exponentiation
```

### Test (`daily_codes/test_fundamentals.py`)
```python
from fundamentals import check_type_and_math

def test_check_type_and_math():
    assert check_type_and_math("2", 3) == 8 # 2^3
```

---

## 2. Control Flow

### Theory
- **Conditionals:** `if`, `elif`, `else` to make decisions.
- **Ternary:** `x if condition else y`.
- **Loops:** `for` (iterate sequences/range), `while` (condition-based).
- **Control:** `break` (exit loop), `continue` (skip iteration), `pass` (do nothing).

### Example (`daily_codes/control.py`)
```python
def sum_evens_up_to(limit):
    total = 0
    for i in range(limit + 1):
        if i % 2 != 0:
            continue
        total += i
    return total
```

### Test (`daily_codes/test_control.py`)
```python
from control import sum_evens_up_to

def test_sum_evens():
    assert sum_evens_up_to(4) == 6 # 0 + 2 + 4
```

---

## 3. Built-in Data Structures

### Theory
- **Strings:** Immutable text. Methods: `.upper()`, `.split()`. Indexing `[0]`, Slicing `[start:stop]`.
- **Lists:** Mutable, ordered `[]`. Methods: `.append()`, `.pop()`.
- **Tuples:** Immutable, ordered `()`.
- **Dictionaries:** Mutable, key-value pairs `{}`. Keys must be immutable.
- **Sets:** Unordered, unique items `{}`. Supports math `.union()`.

### Example (`daily_codes/data_structs.py`)
```python
def manipulate_data(my_list):
    my_list.append("new")
    my_tuple = tuple(my_list)
    my_set = set([1, 2, 2, 3])
    my_dict = {"items": my_tuple, "unique_count": len(my_set)}
    return my_dict
```

### Test (`daily_codes/test_data_structs.py`)
```python
from data_structs import manipulate_data

def test_manipulate_data():
    res = manipulate_data([1])
    assert res["items"] == (1, "new")
    assert res["unique_count"] == 3
```

---

## 4. Functions & Scope

### Theory
- **Functions:** Reusable code blocks defined with `def`.
- **Arguments:** Positional, Default (`x=10`), `*args` (Tuple of arguments), `**kwargs` (Dict of keywords).
- **Scope (LEGB):** Local, Enclosing, Global, Built-in.
- **Lambda:** Anonymous inline functions (e.g., `lambda x: x * 2`).
- **Higher-Order:** `map()`, `filter()`.

### Example (`daily_codes/funcs.py`)
```python
def apply_operation(operation_lambda, *args, **kwargs):
    multiplier = kwargs.get("multiplier", 1)
    return [operation_lambda(x) * multiplier for x in args]
```

### Test (`daily_codes/test_funcs.py`)
```python
from funcs import apply_operation

def test_apply_operation():
    res = apply_operation(lambda x: x + 1, 1, 2, 3, multiplier=2)
    assert res == [4, 6, 8] # (1+1)*2, (2+1)*2, (3+1)*2
```

---

## 5. Comprehensions & Advanced Iteration

### Theory
- **Comprehensions:** Concise loops for Lists `[x for x in data]`, Dicts `{k:v for...}`, Sets `{x for...}`.
- **Generator Expr:** `(x for...)` lazily evaluates, saving memory.
- **Iteration Utils:** `zip()` combines lists, `enumerate()` gives index+value.

### Example (`daily_codes/comprehensions.py`)
```python
def zip_to_dict(keys, values):
    return {k: v for k, v in zip(keys, values) if v is not None}
```

### Test (`daily_codes/test_comprehensions.py`)
```python
from comprehensions import zip_to_dict

def test_zip_to_dict():
    res = zip_to_dict(['a', 'b'], [1, None])
    assert res == {'a': 1}
```

---

## 6. Modules, Packages & Virtual Environments

### Theory
- **Modules:** `.py` files. Import via `import math` or `from os import path`.
- **Main Guard:** `if __name__ == "__main__":` runs code only when executed directly.
- **Virtual Envs:** `python -m venv env` creates an isolated space for dependencies (`pip install`).

*(Note: No test snippet for env setup, as it's a CLI workflow!)*

---

## 7. File Handling & I/O

### Theory
- **Basic:** `open(file, mode)` where modes are `r` (read), `w` (write), `a` (append).
- **Context Managers:** `with open(...) as f:` auto-closes files.
- **JSON:** `json.dump()` / `json.load()`.

### Example (`daily_codes/files.py`)
```python
import json

def write_and_read_json(filepath, data):
    with open(filepath, 'w') as f:
        json.dump(data, f)
    with open(filepath, 'r') as f:
        return json.load(f)
```

### Test (`daily_codes/test_files.py`)
```python
import os
from files import write_and_read_json

def test_json():
    filepath = "temp.json"
    res = write_and_read_json(filepath, {"name": "Aditya"})
    assert res["name"] == "Aditya"
    os.remove(filepath)
```

---

## 8. Error & Exception Handling

### Theory
- **Handling:** `try`, `except Exception as e:`, `else`, `finally`.
- **Raising:** `raise ValueError("Invalid")`.
- **Assertions:** `assert x > 0, "x must be positive"`.

### Example (`daily_codes/errors.py`)
```python
def strict_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Div/0"
```

### Test (`daily_codes/test_errors.py`)
```python
from errors import strict_divide

def test_strict_divide():
    assert strict_divide(10, 2) == 5.0
    assert strict_divide(10, 0) == "Div/0"
```

---

## 9. Object-Oriented Programming (OOP)

### Theory
- **Classes/Objects:** Blueprints and instances.
- **`__init__`:** Constructor. Uses `self`.
- **Inheritance:** Child classes inherit from parent (`class Dog(Animal):`).
- **Encapsulation:** Private variables `__var`.
- **Polymorphism:** Method overriding.
- **Magic Methods:** `__str__` for string representation.

### Example (`daily_codes/oop_demo.py`)
```python
class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def speak(self):
        return f"{self.name} Barks"
```

### Test (`daily_codes/test_oop_demo.py`)
```python
from oop_demo import Dog

def test_dog():
    d = Dog("Rex")
    assert d.speak() == "Rex Barks"
```

---

## 10. Advanced Python Concepts

### Theory
- **Iterators/Generators:** Classes with `__iter__`/`__next__`, or functions with `yield`.
- **Decorators:** Functions wrapping functions (e.g. `@my_decorator`).
- **Type Hinting:** `def add(a: int, b: int) -> int:`.

### Example (`daily_codes/adv.py`)
```python
def count_up_to(max_val):
    count = 1
    while count <= max_val:
        yield count
        count += 1
```

### Test (`daily_codes/test_adv.py`)
```python
from adv import count_up_to

def test_generator():
    gen = count_up_to(3)
    assert list(gen) == [1, 2, 3]
```

---

## 11. Concurrency, Parallelism & Async

### Theory
- **GIL:** Global Interpreter Lock (restricts multi-threading for CPU tasks).
- **Threading/Multiprocessing:** Modules for concurrent execution.
- **AsyncIO:** `async def`, `await` for I/O bound concurrency.

### Example (`daily_codes/async_demo.py`)
```python
import asyncio

async def fetch_data():
    await asyncio.sleep(0.01)
    return "Data"
```

### Test (`daily_codes/test_async_demo.py`)
```python
import asyncio
from async_demo import fetch_data

def test_fetch_data():
    res = asyncio.run(fetch_data())
    assert res == "Data"
```

---

## 12. Professional Ecosystem & Tooling

### Theory
- **Advanced Structures:** `collections.Counter`, `defaultdict`.
- **Testing/Debugging:** `pytest`, `pdb` (Debugger).
- **Network:** `requests` library to fetch APIs.
- **Logging:** `logging` module instead of prints.

### Example (`daily_codes/ecosystem.py`)
```python
from collections import Counter

def get_most_common(word_list):
    return Counter(word_list).most_common(1)[0][0]
```

### Test (`daily_codes/test_ecosystem.py`)
```python
from ecosystem import get_most_common

def test_most_common():
    assert get_most_common(["apple", "banana", "apple"]) == "apple"
```

---
*End of Guide. Start writing code in the `daily_codes/` directory!*
