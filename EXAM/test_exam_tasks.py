import pytest
from exam_tasks import reverse_string, count_vowels, calculate_average

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
