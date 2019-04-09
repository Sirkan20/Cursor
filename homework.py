"""
This is a list of functions that should be completed.
"""


from typing import Any
from typing import List
import string


class OurAwesomeException(Exception):

    pass


def is_two_object_has_same_value(first: Any, second: Any):
    """
    If @first and @second has same value should return True
    In another case should return False
    """
    if first == second:
        return True
    else:
        return False


def is_two_objects_has_same_type(first: Any, second: Any):
    """
    If @first and @second has same type should return True
    In another case should return False
    """
    if type(first) == type(second):
        return True
    else:
        return False


def is_two_objects_is_the_same_objects(first: Any, second: Any):
    """
    If @first and @second has same type should return True
    In another case should return False
    """

    if first is second:
        return True
    else:
        return False


def multiple_ints(first_value: int, second_value: int):
    """
    Should calculate product of all args.
    if first_value or second_value is not int should raise ValueError

    Raises:
        ValueError

    Params:
        first_value: value for multiply
        second_value
    Returns:
        Product of elements
    """
    if type(first_value) != type(int) or type(second_value) != type(int):
        raise ValueError
    else:
        product_of_elements = first_value * second_value

    return product_of_elements


def multiple_ints_with_conversion(first_value: Any, second_value: Any):
    """
    If possible to convert arguments to int value - convert and multiply them.
    If it is impossible raise OurAwesomeException

    Args:
        first_value: number for multiply
        second_value: number for multiply

    Raises:
        OurAwesomeException

    Returns: multiple of two numbers.

    Examples:
        multiple_ints_with_conversion(6, 6)
        >>> 36
        multiple_ints_with_conversion(2, 2.0)
        >>> 4
        multiple_ints_with_conversion("12", 1)
        >>> 12
        try:
            multiple_ints_with_conversion("Hello", 2)
        except ValueError:
            print("Not valid input data")
        >>> "Not valid input data"
    """
    if type(first_value) is not int or type(second_value) is not int:
        raise ValueError()
    return first_value * second_value


def is_word_in_text(word: str, text: str):
    """
    If text contain word return True
    In another case return False.

    Args:
        word: Searchable substring
        text: Text for searching

    Examples:
        is_word_in_text("Hello", "Hello word")
        >>> True
        is_word_in_text("Glad", "Nice to meet you ")
        >>> False
    """
    if word in text:
        return True
    else:
        return False


def some_loop_exercise() -> list:
    """
    Use loop to create list that contain int values from 0 to 12 except 6 and 7
    """
    list_of_loop = []
    for i in range(13):
        if i == 6 or i == 7:
            continue
        list_of_loop.append(i)
    return list_of_loop


def remove_from_list_all_negative_numbers(data: List[int]):
    """
    Use loops to solve this task.
    You could use data.remove(negative_number) to solve this issue.
    Also you could create new list with only positive numbers.
    Examples:
        remove_from_list_all_negative_numbers([1, 5, -7, 8, -1])
        >>> [1, 5, 8]
    """
    remove_negativ = [item for item in data if item >= 0]
    return remove_negativ


def alphabet():
    """
    Create dict which keys is alphabetic characters. And values their number in alphabet
    Notes You could see an implementaion of this one in test, but create another one
    Examples:
        alphabet()
        >>> {"a": 1, "b": 2 ...}
    """
    dict_abc = dict()
    i = 1
    for c in string.ascii_letters:
        dict_abc[i] = c
        i = i + 1
        if i > 26:
            break
    return dict_abc


def simple_sort(data: List[int]):
    """
    Sort list of ints without using built-in methods.
    Examples:
        simple_sort([2, 9, 6, 7, 3, 2, 1])
        >>> [1, 2, 2, 3, 6, 7, 9]
    Returns:
    """
    sortlist = []
    while data:
        m = min(data)  # using the built-in 'min' function
        data.remove(m)
        sortlist.append(m)

    return sortlist
