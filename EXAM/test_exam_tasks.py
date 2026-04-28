import pytest
from exam_tasks import reverse_string, count_vowels, calculate_average, is_even, is_palindrome, find_maximum
from exam_tasks import (
    reverse_string,
    count_vowels,
    calculate_average,
    return_42,
    return_true,
    return_false,
    sum_two,
    multiply_by_10,
    divide_by_2,
    get_remainder,
    power,
    is_equal,
    is_not_equal,
    is_greater,
    is_less,
    is_even,
    is_odd,
    concat_strings,
    str_to_int,
    int_to_str,
    list_to_tuple,
    tuple_to_list,
    get_third,
    get_last_n,
    remove_last,
    insert_first,
    has_substring,
    count_occurrences,
    find_index,
    capitalize_str,
    title_case,
    swap_case,
    is_alnum,
    is_alpha,
    is_digit,
    replace_char,
    split_string,
    join_list,
    get_list_max,
    get_list_min,
    sort_list,
    reverse_list,
    sum_list,
    clear_list,
    get_dict_keys,
    get_dict_values,
    get_dict_items,
    pop_dict_key,
    update_dict,
    set_intersection,
    set_union,
    set_difference,
    is_subset,
    bool_and,
    bool_or,
    xor,
    is_int,
    is_string,
    is_float,
    is_list,
    is_dict,
    round_num,
    return_none,
)

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
# --- Tests for Task 4: return_42 ---
def test_return_42_0():
    assert return_42() == 42

# --- Tests for Task 5: return_true ---
def test_return_true_0():
    assert return_true() == True

# --- Tests for Task 6: return_false ---
def test_return_false_0():
    assert return_false() == False

# --- Tests for Task 7: sum_two ---
def test_sum_two_0():
    assert sum_two(5, 3) == 8
def test_sum_two_1():
    assert sum_two(0, 0) == 0

# --- Tests for Task 8: multiply_by_10 ---
def test_multiply_by_10_0():
    assert multiply_by_10(5) == 50
def test_multiply_by_10_1():
    assert multiply_by_10(2) == 20

# --- Tests for Task 9: divide_by_2 ---
def test_divide_by_2_0():
    assert divide_by_2(10) == 5.0
def test_divide_by_2_1():
    assert divide_by_2(3) == 1.5

# --- Tests for Task 10: get_remainder ---
def test_get_remainder_0():
    assert get_remainder(10, 3) == 1
def test_get_remainder_1():
    assert get_remainder(10, 2) == 0

# --- Tests for Task 11: power ---
def test_power_0():
    assert power(2, 3) == 8
def test_power_1():
    assert power(5, 2) == 25

# --- Tests for Task 12: is_equal ---
def test_is_equal_0():
    assert is_equal(5, 5) == True
def test_is_equal_1():
    assert is_equal(3, 4) == False

# --- Tests for Task 13: is_not_equal ---
def test_is_not_equal_0():
    assert is_not_equal(5, 5) == False
def test_is_not_equal_1():
    assert is_not_equal(3, 4) == True

# --- Tests for Task 14: is_greater ---
def test_is_greater_0():
    assert is_greater(5, 3) == True
def test_is_greater_1():
    assert is_greater(3, 5) == False

# --- Tests for Task 15: is_less ---
def test_is_less_0():
    assert is_less(3, 5) == True
def test_is_less_1():
    assert is_less(5, 3) == False

# --- Tests for Task 16: is_even ---
def test_is_even_0():
    assert is_even(4) == True
def test_is_even_1():
    assert is_even(5) == False

# --- Tests for Task 17: is_odd ---
def test_is_odd_0():
    assert is_odd(4) == False
def test_is_odd_1():
    assert is_odd(5) == True

# --- Tests for Task 18: concat_strings ---
def test_concat_strings_0():
    assert concat_strings('a', 'b') == 'ab'
def test_concat_strings_1():
    assert concat_strings('hello', 'world') == 'helloworld'

# --- Tests for Task 19: str_to_int ---
def test_str_to_int_0():
    assert str_to_int('42') == 42
def test_str_to_int_1():
    assert str_to_int('10') == 10

# --- Tests for Task 20: int_to_str ---
def test_int_to_str_0():
    assert int_to_str(42) == '42'
def test_int_to_str_1():
    assert int_to_str(10) == '10'

# --- Tests for Task 21: list_to_tuple ---
def test_list_to_tuple_0():
    assert list_to_tuple([1, 2]) == (1, 2)
def test_list_to_tuple_1():
    assert list_to_tuple([]) == ()

# --- Tests for Task 22: tuple_to_list ---
def test_tuple_to_list_0():
    assert tuple_to_list((1, 2)) == [1, 2]
def test_tuple_to_list_1():
    assert tuple_to_list(()) == []

# --- Tests for Task 23: get_third ---
def test_get_third_0():
    assert get_third([1, 2, 3]) == 3
def test_get_third_1():
    assert get_third(['a', 'b', 'c', 'd']) == 'c'

# --- Tests for Task 24: get_last_n ---
def test_get_last_n_0():
    assert get_last_n([1, 2, 3, 4], 2) == [3, 4]

# --- Tests for Task 25: remove_last ---
def test_remove_last_0():
    assert remove_last([1, 2, 3]) == 3

# --- Tests for Task 26: insert_first ---
def test_insert_first_0():
    assert insert_first([2, 3], 1) == [1, 2, 3]

# --- Tests for Task 27: has_substring ---
def test_has_substring_0():
    assert has_substring('hello', 'ell') == True
def test_has_substring_1():
    assert has_substring('hello', 'a') == False

# --- Tests for Task 28: count_occurrences ---
def test_count_occurrences_0():
    assert count_occurrences('hello', 'l') == 2
def test_count_occurrences_1():
    assert count_occurrences('banana', 'a') == 3

# --- Tests for Task 29: find_index ---
def test_find_index_0():
    assert find_index('hello', 'e') == 1
def test_find_index_1():
    assert find_index('hello', 'a') == -1

# --- Tests for Task 30: capitalize_str ---
def test_capitalize_str_0():
    assert capitalize_str('hello') == 'Hello'
def test_capitalize_str_1():
    assert capitalize_str('world') == 'World'

# --- Tests for Task 31: title_case ---
def test_title_case_0():
    assert title_case('hello world') == 'Hello World'

# --- Tests for Task 32: swap_case ---
def test_swap_case_0():
    assert swap_case('HeLlO') == 'hElLo'

# --- Tests for Task 33: is_alnum ---
def test_is_alnum_0():
    assert is_alnum('a1') == True
def test_is_alnum_1():
    assert is_alnum('a-1') == False

# --- Tests for Task 34: is_alpha ---
def test_is_alpha_0():
    assert is_alpha('abc') == True
def test_is_alpha_1():
    assert is_alpha('a1') == False

# --- Tests for Task 35: is_digit ---
def test_is_digit_0():
    assert is_digit('123') == True
def test_is_digit_1():
    assert is_digit('a1') == False

# --- Tests for Task 36: replace_char ---
def test_replace_char_0():
    assert replace_char('apple', 'p', 'b') == 'abble'

# --- Tests for Task 37: split_string ---
def test_split_string_0():
    assert split_string('a,b', ',') == ['a', 'b']

# --- Tests for Task 38: join_list ---
def test_join_list_0():
    assert join_list(['a', 'b'], ',') == 'a,b'

# --- Tests for Task 39: get_list_max ---
def test_get_list_max_0():
    assert get_list_max([1, 5, 2]) == 5

# --- Tests for Task 40: get_list_min ---
def test_get_list_min_0():
    assert get_list_min([1, 5, 2]) == 1

# --- Tests for Task 41: sort_list ---
def test_sort_list_0():
    assert sort_list([3, 1, 2]) == [1, 2, 3]

# --- Tests for Task 42: reverse_list ---
def test_reverse_list_0():
    assert reverse_list([1, 2, 3]) == [3, 2, 1]

# --- Tests for Task 43: sum_list ---
def test_sum_list_0():
    assert sum_list([1, 2, 3]) == 6

# --- Tests for Task 44: clear_list ---
def test_clear_list_0():
    assert clear_list([1, 2]) == []

# --- Tests for Task 45: get_dict_keys ---
def test_get_dict_keys_0():
    assert get_dict_keys({'a': 1, 'b': 2}) == ['a', 'b']

# --- Tests for Task 46: get_dict_values ---
def test_get_dict_values_0():
    assert get_dict_values({'a': 1, 'b': 2}) == [1, 2]

# --- Tests for Task 47: get_dict_items ---
def test_get_dict_items_0():
    assert get_dict_items({'a': 1}) == [('a', 1)]

# --- Tests for Task 48: pop_dict_key ---
def test_pop_dict_key_0():
    assert pop_dict_key({'a': 1}, 'a') == 1

# --- Tests for Task 49: update_dict ---
def test_update_dict_0():
    assert update_dict({'a': 1}, {'b': 2}) == {'a': 1, 'b': 2}

# --- Tests for Task 50: set_intersection ---
def test_set_intersection_0():
    assert set_intersection({1, 2}, {2, 3}) == {2}

# --- Tests for Task 51: set_union ---
def test_set_union_0():
    assert set_union({1}, {2}) == {1, 2}

# --- Tests for Task 52: set_difference ---
def test_set_difference_0():
    assert set_difference({1, 2}, {2, 3}) == {1}

# --- Tests for Task 53: is_subset ---
def test_is_subset_0():
    assert is_subset({1}, {1, 2}) == True
def test_is_subset_1():
    assert is_subset({3}, {1, 2}) == False

# --- Tests for Task 54: bool_and ---
def test_bool_and_0():
    assert bool_and(True, True, False) == False

# --- Tests for Task 55: bool_or ---
def test_bool_or_0():
    assert bool_or(False, False, True) == True

# --- Tests for Task 56: xor ---
def test_xor_0():
    assert xor(True, False) == True
def test_xor_1():
    assert xor(True, True) == False

# --- Tests for Task 57: is_int ---
def test_is_int_0():
    assert is_int(5) == True
def test_is_int_1():
    assert is_int('5') == False

# --- Tests for Task 58: is_string ---
def test_is_string_0():
    assert is_string('hello') == True
def test_is_string_1():
    assert is_string(5) == False

# --- Tests for Task 59: is_float ---
def test_is_float_0():
    assert is_float(5.0) == True
def test_is_float_1():
    assert is_float(5) == False

# --- Tests for Task 60: is_list ---
def test_is_list_0():
    assert is_list([]) == True
def test_is_list_1():
    assert is_list({}) == False

# --- Tests for Task 61: is_dict ---
def test_is_dict_0():
    assert is_dict({}) == True
def test_is_dict_1():
    assert is_dict([]) == False

# --- Tests for Task 62: round_num ---
def test_round_num_0():
    assert round_num(5.4) == 5
def test_round_num_1():
    assert round_num(5.6) == 6

# --- Tests for Task 63: return_none ---
def test_return_none_0():
    assert return_none() == None
