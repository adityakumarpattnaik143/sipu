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

## Question 7: Subtract Two Numbers

**Task:** Write a function `subtract_numbers(a, b)` that will subtract `b` from `a`.

**Starter Code:**
```python
def subtract_numbers(a, b):
    # Your code here
    pass
```

**Test Cases:**
```python
assert subtract_numbers(10, 5) == 5
assert subtract_numbers(0, 0) == 0
print("Question 7 passed!")
```

<details>
<summary><b>Click here to see the Solution</b></summary>

```python
def subtract_numbers(a, b):
    return a - b
```
</details>

---

## Question 8: Multiply Two Numbers

**Task:** Write a function `multiply_numbers(a, b)` that will return the product of `a` and `b`.

**Starter Code:**
```python
def multiply_numbers(a, b):
    # Your code here
    pass
```

**Test Cases:**
```python
assert multiply_numbers(3, 4) == 12
assert multiply_numbers(0, 5) == 0
print("Question 8 passed!")
```

<details>
<summary><b>Click here to see the Solution</b></summary>

```python
def multiply_numbers(a, b):
    return a * b
```
</details>

---

## Question 9: Divide Two Numbers

**Task:** Write a function `divide_numbers(a, b)` that will return the float division of `a` by `b`. Assume `b` is not 0.

**Starter Code:**
```python
def divide_numbers(a, b):
    # Your code here
    pass
```

**Test Cases:**
```python
assert divide_numbers(10, 2) == 5.0
assert divide_numbers(7, 2) == 3.5
print("Question 9 passed!")
```

<details>
<summary><b>Click here to see the Solution</b></summary>

```python
def divide_numbers(a, b):
    return a / b
```
</details>

---

## Question 10: Square a Number

**Task:** Write a function `square_number(n)` that will return `n` squared.

**Starter Code:**
```python
def square_number(n):
    # Your code here
    pass
```

**Test Cases:**
```python
assert square_number(4) == 16
assert square_number(5) == 25
print("Question 10 passed!")
```

<details>
<summary><b>Click here to see the Solution</b></summary>

```python
def square_number(n):
    return n ** 2
```
</details>

---

## Question 11: Cube a Number

**Task:** Write a function `cube_number(n)` that will return `n` cubed.

**Starter Code:**
```python
def cube_number(n):
    # Your code here
    pass
```

**Test Cases:**
```python
assert cube_number(2) == 8
assert cube_number(3) == 27
print("Question 11 passed!")
```

<details>
<summary><b>Click here to see the Solution</b></summary>

```python
def cube_number(n):
    return n ** 3
```
</details>

---

## Question 12: Check if Positive

**Task:** Write a function `is_positive(n)` that will return `True` if `n` > 0, else `False`.

**Starter Code:**
```python
def is_positive(n):
    # Your code here
    pass
```

**Test Cases:**
```python
assert is_positive(5) == True
assert is_positive(-2) == False
assert is_positive(0) == False
print("Question 12 passed!")
```

<details>
<summary><b>Click here to see the Solution</b></summary>

```python
def is_positive(n):
    return n > 0
```
</details>

---

## Question 13: Check if Negative

**Task:** Write a function `is_negative(n)` that will return `True` if `n` < 0, else `False`.

**Starter Code:**
```python
def is_negative(n):
    # Your code here
    pass
```

**Test Cases:**
```python
assert is_negative(-5) == True
assert is_negative(2) == False
assert is_negative(0) == False
print("Question 13 passed!")
```

<details>
<summary><b>Click here to see the Solution</b></summary>

```python
def is_negative(n):
    return n < 0
```
</details>

---

## Question 14: Check if Zero

**Task:** Write a function `is_zero(n)` that will return `True` if `n` == 0, else `False`.

**Starter Code:**
```python
def is_zero(n):
    # Your code here
    pass
```

**Test Cases:**
```python
assert is_zero(0) == True
assert is_zero(1) == False
print("Question 14 passed!")
```

<details>
<summary><b>Click here to see the Solution</b></summary>

```python
def is_zero(n):
    return n == 0
```
</details>

---

## Question 15: Return Empty String

**Task:** Write a function `get_empty_string()` that will return an empty string.

**Starter Code:**
```python
def get_empty_string():
    # Your code here
    pass
```

**Test Cases:**
```python
assert get_empty_string() == ''
print("Question 15 passed!")
```

<details>
<summary><b>Click here to see the Solution</b></summary>

```python
def get_empty_string():
    return ''
```
</details>

---

## Question 16: Get String Length

**Task:** Write a function `get_string_length(s)` that will return the length of the string `s`.

**Starter Code:**
```python
def get_string_length(s):
    # Your code here
    pass
```

**Test Cases:**
```python
assert get_string_length('hello') == 5
assert get_string_length('') == 0
print("Question 16 passed!")
```

<details>
<summary><b>Click here to see the Solution</b></summary>

```python
def get_string_length(s):
    return len(s)
```
</details>

---

## Question 17: Uppercase String

**Task:** Write a function `to_uppercase(s)` that will return the uppercase version of `s`.

**Starter Code:**
```python
def to_uppercase(s):
    # Your code here
    pass
```

**Test Cases:**
```python
assert to_uppercase('hi') == 'HI'
assert to_uppercase('HELLO') == 'HELLO'
print("Question 17 passed!")
```

<details>
<summary><b>Click here to see the Solution</b></summary>

```python
def to_uppercase(s):
    return s.upper()
```
</details>

---

## Question 18: Lowercase String

**Task:** Write a function `to_lowercase(s)` that will return the lowercase version of `s`.

**Starter Code:**
```python
def to_lowercase(s):
    # Your code here
    pass
```

**Test Cases:**
```python
assert to_lowercase('HI') == 'hi'
assert to_lowercase('hello') == 'hello'
print("Question 18 passed!")
```

<details>
<summary><b>Click here to see the Solution</b></summary>

```python
def to_lowercase(s):
    return s.lower()
```
</details>

---

## Question 19: First Character

**Task:** Write a function `get_first_char(s)` that will return the first character of `s`. Assume length >= 1.

**Starter Code:**
```python
def get_first_char(s):
    # Your code here
    pass
```

**Test Cases:**
```python
assert get_first_char('apple') == 'a'
assert get_first_char('Z') == 'Z'
print("Question 19 passed!")
```

<details>
<summary><b>Click here to see the Solution</b></summary>

```python
def get_first_char(s):
    return s[0]
```
</details>

---

## Question 20: Last Character

**Task:** Write a function `get_last_char(s)` that will return the last character of `s`. Assume length >= 1.

**Starter Code:**
```python
def get_last_char(s):
    # Your code here
    pass
```

**Test Cases:**
```python
assert get_last_char('apple') == 'e'
assert get_last_char('A') == 'A'
print("Question 20 passed!")
```

<details>
<summary><b>Click here to see the Solution</b></summary>

```python
def get_last_char(s):
    return s[-1]
```
</details>

---

## Question 21: Repeat String

**Task:** Write a function `repeat_string(s, n)` that will return the string `s` repeated `n` times.

**Starter Code:**
```python
def repeat_string(s, n):
    # Your code here
    pass
```

**Test Cases:**
```python
assert repeat_string('a', 3) == 'aaa'
assert repeat_string('hi', 2) == 'hihi'
print("Question 21 passed!")
```

<details>
<summary><b>Click here to see the Solution</b></summary>

```python
def repeat_string(s, n):
    return s * n
```
</details>

---

## Question 22: Return Empty List

**Task:** Write a function `get_empty_list()` that will return an empty list.

**Starter Code:**
```python
def get_empty_list():
    # Your code here
    pass
```

**Test Cases:**
```python
assert get_empty_list() == []
print("Question 22 passed!")
```

<details>
<summary><b>Click here to see the Solution</b></summary>

```python
def get_empty_list():
    return []
```
</details>

---

## Question 23: List Length

**Task:** Write a function `get_list_length(lst)` that will return the number of elements in `lst`.

**Starter Code:**
```python
def get_list_length(lst):
    # Your code here
    pass
```

**Test Cases:**
```python
assert get_list_length([1, 2, 3]) == 3
assert get_list_length([]) == 0
print("Question 23 passed!")
```

<details>
<summary><b>Click here to see the Solution</b></summary>

```python
def get_list_length(lst):
    return len(lst)
```
</details>

---

## Question 24: First List Element

**Task:** Write a function `get_first_element(lst)` that will return the first element. Assume length >= 1.

**Starter Code:**
```python
def get_first_element(lst):
    # Your code here
    pass
```

**Test Cases:**
```python
assert get_first_element([10, 20]) == 10
print("Question 24 passed!")
```

<details>
<summary><b>Click here to see the Solution</b></summary>

```python
def get_first_element(lst):
    return lst[0]
```
</details>

---

## Question 25: Last List Element

**Task:** Write a function `get_last_element(lst)` that will return the last element. Assume length >= 1.

**Starter Code:**
```python
def get_last_element(lst):
    # Your code here
    pass
```

**Test Cases:**
```python
assert get_last_element([10, 20]) == 20
print("Question 25 passed!")
```

<details>
<summary><b>Click here to see the Solution</b></summary>

```python
def get_last_element(lst):
    return lst[-1]
```
</details>

---

## Question 26: Append to List

**Task:** Write a function `append_element(lst, elem)` that will append `elem` to `lst` and return `lst`.

**Starter Code:**
```python
def append_element(lst, elem):
    # Your code here
    pass
```

**Test Cases:**
```python
assert append_element([1], 2) == [1, 2]
print("Question 26 passed!")
```

<details>
<summary><b>Click here to see the Solution</b></summary>

```python
def append_element(lst, elem):
    lst.append(elem)
    return lst
```
</details>

---

## Question 27: Check if Empty List

**Task:** Write a function `is_list_empty(lst)` that will return `True` if `lst` is empty, else `False`.

**Starter Code:**
```python
def is_list_empty(lst):
    # Your code here
    pass
```

**Test Cases:**
```python
assert is_list_empty([]) == True
assert is_list_empty([1]) == False
print("Question 27 passed!")
```

<details>
<summary><b>Click here to see the Solution</b></summary>

```python
def is_list_empty(lst):
    return len(lst) == 0
```
</details>

---

## Question 28: Both True

**Task:** Write a function `both_true(a, b)` that will return `True` if both `a` and `b` are `True`.

**Starter Code:**
```python
def both_true(a, b):
    # Your code here
    pass
```

**Test Cases:**
```python
assert both_true(True, True) == True
assert both_true(True, False) == False
print("Question 28 passed!")
```

<details>
<summary><b>Click here to see the Solution</b></summary>

```python
def both_true(a, b):
    return a and b
```
</details>

---

## Question 29: Either True

**Task:** Write a function `either_true(a, b)` that will return `True` if either `a` or `b` is `True`.

**Starter Code:**
```python
def either_true(a, b):
    # Your code here
    pass
```

**Test Cases:**
```python
assert either_true(True, False) == True
assert either_true(False, False) == False
print("Question 29 passed!")
```

<details>
<summary><b>Click here to see the Solution</b></summary>

```python
def either_true(a, b):
    return a or b
```
</details>

---

## Question 30: Not True

**Task:** Write a function `not_true(a)` that will return the logical opposite of boolean `a`.

**Starter Code:**
```python
def not_true(a):
    # Your code here
    pass
```

**Test Cases:**
```python
assert not_true(True) == False
assert not_true(False) == True
print("Question 30 passed!")
```

<details>
<summary><b>Click here to see the Solution</b></summary>

```python
def not_true(a):
    return not a
```
</details>

---

## Question 31: Add Three Numbers

**Task:** Write a function `add_three(a, b, c)` that will return the sum of three numbers.

**Starter Code:**
```python
def add_three(a, b, c):
    # Your code here
    pass
```

**Test Cases:**
```python
assert add_three(1, 2, 3) == 6
print("Question 31 passed!")
```

<details>
<summary><b>Click here to see the Solution</b></summary>

```python
def add_three(a, b, c):
    return a + b + c
```
</details>

---

## Question 32: Average of Two

**Task:** Write a function `average_two(a, b)` that will return the average of `a` and `b` as a float.

**Starter Code:**
```python
def average_two(a, b):
    # Your code here
    pass
```

**Test Cases:**
```python
assert average_two(10, 20) == 15.0
print("Question 32 passed!")
```

<details>
<summary><b>Click here to see the Solution</b></summary>

```python
def average_two(a, b):
    return (a + b) / 2.0
```
</details>

---

## Question 33: Absolute Value

**Task:** Write a function `get_abs(n)` that will return the absolute value of `n`.

**Starter Code:**
```python
def get_abs(n):
    # Your code here
    pass
```

**Test Cases:**
```python
assert get_abs(-5) == 5
assert get_abs(3) == 3
print("Question 33 passed!")
```

<details>
<summary><b>Click here to see the Solution</b></summary>

```python
def get_abs(n):
    return abs(n)
```
</details>

---

## Question 34: Is Divisible By 3

**Task:** Write a function `is_divisible_by_3(n)` that will return `True` if `n` is divisible by 3.

**Starter Code:**
```python
def is_divisible_by_3(n):
    # Your code here
    pass
```

**Test Cases:**
```python
assert is_divisible_by_3(9) == True
assert is_divisible_by_3(10) == False
print("Question 34 passed!")
```

<details>
<summary><b>Click here to see the Solution</b></summary>

```python
def is_divisible_by_3(n):
    return n % 3 == 0
```
</details>

---

## Question 35: Is Divisible By 5

**Task:** Write a function `is_divisible_by_5(n)` that will return `True` if `n` is divisible by 5.

**Starter Code:**
```python
def is_divisible_by_5(n):
    # Your code here
    pass
```

**Test Cases:**
```python
assert is_divisible_by_5(10) == True
assert is_divisible_by_5(12) == False
print("Question 35 passed!")
```

<details>
<summary><b>Click here to see the Solution</b></summary>

```python
def is_divisible_by_5(n):
    return n % 5 == 0
```
</details>

---

## Question 36: Starts With A

**Task:** Write a function `starts_with_a(s)` that will return `True` if string `s` starts with 'A' or 'a'.

**Starter Code:**
```python
def starts_with_a(s):
    # Your code here
    pass
```

**Test Cases:**
```python
assert starts_with_a('Apple') == True
assert starts_with_a('banana') == False
print("Question 36 passed!")
```

<details>
<summary><b>Click here to see the Solution</b></summary>

```python
def starts_with_a(s):
    return s.lower().startswith('a')
```
</details>

---

## Question 37: Ends With Z

**Task:** Write a function `ends_with_z(s)` that will return `True` if string `s` ends with 'Z' or 'z'.

**Starter Code:**
```python
def ends_with_z(s):
    # Your code here
    pass
```

**Test Cases:**
```python
assert ends_with_z('buzz') == True
assert ends_with_z('cat') == False
print("Question 37 passed!")
```

<details>
<summary><b>Click here to see the Solution</b></summary>

```python
def ends_with_z(s):
    return s.lower().endswith('z')
```
</details>

---

## Question 38: Strip Whitespace

**Task:** Write a function `strip_string(s)` that will remove leading and trailing whitespace.

**Starter Code:**
```python
def strip_string(s):
    # Your code here
    pass
```

**Test Cases:**
```python
assert strip_string(' hi ') == 'hi'
print("Question 38 passed!")
```

<details>
<summary><b>Click here to see the Solution</b></summary>

```python
def strip_string(s):
    return s.strip()
```
</details>

---

## Question 39: Replace Space with Dash

**Task:** Write a function `replace_space(s)` that will replace all spaces in `s` with a dash '-'.

**Starter Code:**
```python
def replace_space(s):
    # Your code here
    pass
```

**Test Cases:**
```python
assert replace_space('a b') == 'a-b'
print("Question 39 passed!")
```

<details>
<summary><b>Click here to see the Solution</b></summary>

```python
def replace_space(s):
    return s.replace(' ', '-')
```
</details>

---

## Question 40: Return Empty Dict

**Task:** Write a function `get_empty_dict()` that will return an empty dictionary.

**Starter Code:**
```python
def get_empty_dict():
    # Your code here
    pass
```

**Test Cases:**
```python
assert get_empty_dict() == {}
print("Question 40 passed!")
```

<details>
<summary><b>Click here to see the Solution</b></summary>

```python
def get_empty_dict():
    return {}
```
</details>

---

## Question 41: Get Dict Value

**Task:** Write a function `get_dict_value(d, k)` that will return value for key `k` in dictionary `d`. Assume `k` exists.

**Starter Code:**
```python
def get_dict_value(d, k):
    # Your code here
    pass
```

**Test Cases:**
```python
assert get_dict_value({'a': 1}, 'a') == 1
print("Question 41 passed!")
```

<details>
<summary><b>Click here to see the Solution</b></summary>

```python
def get_dict_value(d, k):
    return d[k]
```
</details>

---

## Question 42: Check Key Exists

**Task:** Write a function `key_exists(d, k)` that will return `True` if `k` is in `d`.

**Starter Code:**
```python
def key_exists(d, k):
    # Your code here
    pass
```

**Test Cases:**
```python
assert key_exists({'a': 1}, 'a') == True
assert key_exists({'a': 1}, 'b') == False
print("Question 42 passed!")
```

<details>
<summary><b>Click here to see the Solution</b></summary>

```python
def key_exists(d, k):
    return k in d
```
</details>

---

## Question 43: Count to N

**Task:** Write a function `count_to_n(n)` that will return a list of integers from 1 to `n` inclusive.

**Starter Code:**
```python
def count_to_n(n):
    # Your code here
    pass
```

**Test Cases:**
```python
assert count_to_n(3) == [1, 2, 3]
print("Question 43 passed!")
```

<details>
<summary><b>Click here to see the Solution</b></summary>

```python
def count_to_n(n):
    return list(range(1, n + 1))
```
</details>

---

## Question 44: Count from 0 to N-1

**Task:** Write a function `count_zero_to_n(n)` that will return a list of integers from 0 to `n-1`.

**Starter Code:**
```python
def count_zero_to_n(n):
    # Your code here
    pass
```

**Test Cases:**
```python
assert count_zero_to_n(3) == [0, 1, 2]
print("Question 44 passed!")
```

<details>
<summary><b>Click here to see the Solution</b></summary>

```python
def count_zero_to_n(n):
    return list(range(n))
```
</details>

---

## Question 45: Max of Two

**Task:** Write a function `max_of_two(a, b)` that will return the larger of `a` and `b`.

**Starter Code:**
```python
def max_of_two(a, b):
    # Your code here
    pass
```

**Test Cases:**
```python
assert max_of_two(5, 10) == 10
print("Question 45 passed!")
```

<details>
<summary><b>Click here to see the Solution</b></summary>

```python
def max_of_two(a, b):
    return max(a, b)
```
</details>

---

## Question 46: Min of Two

**Task:** Write a function `min_of_two(a, b)` that will return the smaller of `a` and `b`.

**Starter Code:**
```python
def min_of_two(a, b):
    # Your code here
    pass
```

**Test Cases:**
```python
assert min_of_two(5, 10) == 5
print("Question 46 passed!")
```

<details>
<summary><b>Click here to see the Solution</b></summary>

```python
def min_of_two(a, b):
    return min(a, b)
```
</details>

---

## Question 47: Is Even Length

**Task:** Write a function `is_even_length(s)` that will return `True` if the string length is even.

**Starter Code:**
```python
def is_even_length(s):
    # Your code here
    pass
```

**Test Cases:**
```python
assert is_even_length('ab') == True
assert is_even_length('a') == False
print("Question 47 passed!")
```

<details>
<summary><b>Click here to see the Solution</b></summary>

```python
def is_even_length(s):
    return len(s) % 2 == 0
```
</details>

---

## Question 48: Double List

**Task:** Write a function `double_list(lst)` that will return the list concatenated with itself.

**Starter Code:**
```python
def double_list(lst):
    # Your code here
    pass
```

**Test Cases:**
```python
assert double_list([1]) == [1, 1]
print("Question 48 passed!")
```

<details>
<summary><b>Click here to see the Solution</b></summary>

```python
def double_list(lst):
    return lst + lst
```
</details>

---

## Question 49: Add Dict Key

**Task:** Write a function `add_dict_key(d, k, v)` that will add key `k` with value `v` to dict `d` and return `d`.

**Starter Code:**
```python
def add_dict_key(d, k, v):
    # Your code here
    pass
```

**Test Cases:**
```python
assert add_dict_key({}, 'a', 1) == {'a': 1}
print("Question 49 passed!")
```

<details>
<summary><b>Click here to see the Solution</b></summary>

```python
def add_dict_key(d, k, v):
    d[k] = v
    return d
```
</details>

---

## Question 50: Remove First Element

**Task:** Write a function `remove_first(lst)` that will return `lst` after removing the first element. Assume length >= 1.

**Starter Code:**
```python
def remove_first(lst):
    # Your code here
    pass
```

**Test Cases:**
```python
assert remove_first([1, 2]) == [2]
print("Question 50 passed!")
```

<details>
<summary><b>Click here to see the Solution</b></summary>

```python
def remove_first(lst):
    lst.pop(0)
    return lst
```
</details>

---
