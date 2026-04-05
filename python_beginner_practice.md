# Python Beginner Practice: Level 0 Questions

Welcome to the beginner practice guide! This document is designed as a companion to the main Python guide. These "Level 0" questions will help you practice syntax, basic data types, logic, and functions.

Each question includes a **guide**, **starter code**, **test cases**, and the **solution**.

---

## Question 1: Hello World and Basic Output

**Task:** Write a function `greet_user(name)` that takes a string `name` and returns a greeting message in the format: `"Hello, [name]!"`

**Guide:**
- You will need to use string concatenation (e.g., `+`) or f-strings (e.g., `f"..."`).
- Return the resulting string instead of printing it.

**Starter Code:**
```python
def greet_user(name):
    # Your code here
    pass
```

**Test Cases:**
```python
assert greet_user("Alice") == "Hello, Alice!"
assert greet_user("Bob") == "Hello, Bob!"
print("Question 1 passed!")
```

<details>
<summary><b>Click here to see the Solution</b></summary>

```python
def greet_user(name):
    return f"Hello, {name}!"
```
</details>

---

## Question 2: Simple Arithmetic

**Task:** Write a function `calculate_area(length, width)` that returns the area of a rectangle.

**Guide:**
- The area of a rectangle is `length` multiplied by `width`.
- Use the `*` operator.

**Starter Code:**
```python
def calculate_area(length, width):
    # Your code here
    pass
```

**Test Cases:**
```python
assert calculate_area(5, 10) == 50
assert calculate_area(7, 3) == 21
print("Question 2 passed!")
```

<details>
<summary><b>Click here to see the Solution</b></summary>

```python
def calculate_area(length, width):
    return length * width
```
</details>

---

## Question 3: Conditionals - Odd or Even

**Task:** Write a function `is_even(number)` that returns `True` if the number is even, and `False` if it is odd.

**Guide:**
- A number is even if it is divisible by 2 with no remainder.
- Use the modulo operator `%`. If `number % 2 == 0`, it is even.

**Starter Code:**
```python
def is_even(number):
    # Your code here
    pass
```

**Test Cases:**
```python
assert is_even(4) == True
assert is_even(7) == False
assert is_even(0) == True
print("Question 3 passed!")
```

<details>
<summary><b>Click here to see the Solution</b></summary>

```python
def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

# Or the shorter version:
# def is_even(number):
#     return number % 2 == 0
```
</details>

---

## Question 4: Working with Lists

**Task:** Write a function `get_first_and_last(items)` that takes a list and returns a new list containing only the first and last elements.

**Guide:**
- Access the first element using index `0`.
- Access the last element using index `-1`.
- Put them inside a new list `[]` and return it.
- Assume the list has at least one element.

**Starter Code:**
```python
def get_first_and_last(items):
    # Your code here
    pass
```

**Test Cases:**
```python
assert get_first_and_last([1, 2, 3, 4, 5]) == [1, 5]
assert get_first_and_last(["apple", "banana", "cherry"]) == ["apple", "cherry"]
assert get_first_and_last([99]) == [99, 99]
print("Question 4 passed!")
```

<details>
<summary><b>Click here to see the Solution</b></summary>

```python
def get_first_and_last(items):
    return [items[0], items[-1]]
```
</details>

---

## Question 5: Loops - Sum of List

**Task:** Write a function `sum_numbers(numbers)` that takes a list of integers and returns their total sum using a `for` loop. (Do not use the built-in `sum()` function).

**Guide:**
- Create a variable (e.g., `total = 0`) to hold the sum.
- Use a `for num in numbers:` loop.
- Add each `num` to `total`.
- Return `total` at the end.

**Starter Code:**
```python
def sum_numbers(numbers):
    # Your code here
    pass
```

**Test Cases:**
```python
assert sum_numbers([1, 2, 3]) == 6
assert sum_numbers([10, -5, 5]) == 10
assert sum_numbers([]) == 0
print("Question 5 passed!")
```

<details>
<summary><b>Click here to see the Solution</b></summary>

```python
def sum_numbers(numbers):
    total = 0
    for num in numbers:
        total += num
    return total
```
</details>

---

## Question 6: Dictionaries

**Task:** Write a function `get_student_age(student_dict, name)` that takes a dictionary of student names and ages, and returns the age of the specified `name`. If the name is not in the dictionary, return `"Not Found"`.

**Guide:**
- Use the `.get()` method on the dictionary.
- `.get(key, default_value)` allows you to specify a return value if the key does not exist.

**Starter Code:**
```python
def get_student_age(student_dict, name):
    # Your code here
    pass
```

**Test Cases:**
```python
students = {"Alice": 20, "Bob": 22, "Charlie": 19}
assert get_student_age(students, "Alice") == 20
assert get_student_age(students, "David") == "Not Found"
print("Question 6 passed!")
```

<details>
<summary><b>Click here to see the Solution</b></summary>

```python
def get_student_age(student_dict, name):
    return student_dict.get(name, "Not Found")
```
</details>

---

*Keep practicing! The more you write code and solve these small problems, the more naturally the syntax will come to you.*
