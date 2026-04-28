import pytest
from exam_tasks import reverse_string, count_vowels, calculate_average, is_even, is_palindrome, find_maximum

# --- Tests for Task 1: reverse_string ---
def test_reverse_string_normal():
    assert reverse_string("hello") == "olleh"

def test_reverse_string_empty():
    assert reverse_string("") == ""

def test_reverse_string_palindrome():
    assert reverse_string("racecar") == "racecar"

def test_reverse_string_with_spaces():
    assert reverse_string("a b c") == "c b a"


# --- Tests for Task 2: count_vowels ---
def test_count_vowels_lowercase():
    assert count_vowels("apple") == 2

def test_count_vowels_mixed_case():
    assert count_vowels("EDUCATION") == 5

def test_count_vowels_none():
    assert count_vowels("rhythm") == 0

def test_count_vowels_empty():
    assert count_vowels("") == 0


# --- Tests for Task 3: calculate_average ---
def test_calculate_average_normal():
    assert calculate_average([10, 20, 30]) == 20.0

def test_calculate_average_floats():
    assert calculate_average([1.5, 2.5, 5.0]) == 3.0

def test_calculate_average_empty():
    assert calculate_average([]) == 0

def test_calculate_average_single_element():
    assert calculate_average([42]) == 42.0


# --- Tests for Task 4: is_even ---
def test_is_even_true():
    assert is_even(4) is True
    assert is_even(0) is True
    assert is_even(-2) is True

def test_is_even_false():
    assert is_even(7) is False
    assert is_even(1) is False
    assert is_even(-3) is False


# --- Tests for Task 5: is_palindrome ---
def test_is_palindrome_true():
    assert is_palindrome("racecar") is True
    assert is_palindrome("madam") is True
    assert is_palindrome("a") is True
    assert is_palindrome("") is True

def test_is_palindrome_false():
    assert is_palindrome("hello") is False
    assert is_palindrome("python") is False


# --- Tests for Task 6: find_maximum ---
def test_find_maximum_normal():
    assert find_maximum([1, 5, 3, 9, 2]) == 9

def test_find_maximum_negative():
    assert find_maximum([-5, -1, -10]) == -1

def test_find_maximum_empty():
    assert find_maximum([]) is None

def test_find_maximum_single_element():
    assert find_maximum([42]) == 42
