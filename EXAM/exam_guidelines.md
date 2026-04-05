# Exam Guidelines

Welcome to the EXAM section! This folder is designed to test your logic-building skills without worrying about setting up tests or data structures from scratch.

## How It Works

1. **Read the Questions:** Open `exam.md` to find the problem descriptions.
2. **Write the Logic:** Open `exam_tasks.py`. You will see empty functions with a `pass` statement. Replace the `pass` statement with your own logic to solve the problem.
3. **Run the Tests:** You do not need to modify `test_exam_tasks.py`. Once you have written your code in `exam_tasks.py`, open your terminal and run the following command from the root of the project:

   ```bash
   pytest EXAM/
   ```

   The testing framework will automatically run test cases against your code. If your logic is correct, the tests will pass in green. If incorrect, they will fail in red, showing you what output was expected.

---

## Guided Example

To help you understand the workflow, here is an example problem that is *similar* to what you will find in the exam, but not identical.

### Example Problem: Find the Maximum
Write a function `find_maximum(numbers)` that takes a list of numbers and returns the largest number.

### 1. Template (How it looks initially in `exam_tasks.py`):
```python
def find_maximum(numbers):
    # TODO: Write your logic here
    pass
```

### 2. The Tests (How it looks in `test_exam_tasks.py` - Do not change this):
```python
def test_find_maximum():
    from exam_tasks import find_maximum
    assert find_maximum([1, 5, 3]) == 5
    assert find_maximum([-10, -5, -20]) == -5
```

### 3. Your Solution (How you should update `exam_tasks.py`):
```python
def find_maximum(numbers):
    if not numbers:
        return None

    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num

    return max_num
```

Once you save the file and run `pytest EXAM/`, the tests will pass!

Now, head over to `exam.md` and start your exam! Good luck.