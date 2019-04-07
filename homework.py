"""
This is a list of functions that should be completed.
"""

from typing import Any
from typing import List


class OurAwesomeException(Exception):
    pass


def is_two_object_has_same_value(first, second):
    if first == second:
        print(True)
    else:
        print(False)

    pass


def is_two_objects_has_same_type(first, second):
    if type(first) == type(second):
        print(True)
    else:
        print(False)

    pass


def is_two_objects_is_the_same_objects(first, second):
    if first is second:
        print(True)
    else:
        print(False)

    pass


def multiple_ints(first_value, second_value):
    if type(first_value) != type(int) or type(second_value) != type(int):
        raise ValueError
    else:
        product_of_elements = first_value * second_value

    return product_of_elements



def multiple_ints_with_conversion(first_value, second_value):
    try:
        first_value = int(first_value)
        second_value = int(second_value)
        multiple_of_two_numbers = first_value * second_value
        print(multiple_of_two_numbers)
    except ValueError:
        print("OurAwesomeException")
    print('Programs is Done')


def is_word_in_text(word, text):
    if word in text:
        print(True)
    else:
        print(False)
    pass


def some_loop_exercise():
    list_of_loop = []
    for i in range(13):
        if i == 6 or i == 7:
            continue
        list_of_loop.append(i)
    print(list_of_loop)
    """
    Use loop to create list that contain int values from 0 to 12 except 6 and 7
    """
    pass


def remove_from_list_all_negative_numbers(lis):
    remove_all_negative_numbers = [item for item in lis if item >= 0]

    """
    Use loops to solve this task.
    You could use data.remove(negative_number) to solve this issue.
    Also you could create new list with only positive numbers.
    Examples:
        remove_from_list_all_negative_numbers([1, 5, -7, 8, -1])
        >>> [1, 5, 8]
    """
    pass


def alphabet():
    import string


    dict_abc = dict()
    i = 0
    for c in string.ascii_letters:
        dict_abc[i] = c
        i = i + 1
        if i > 25:
            break
    print(dict_abc)
    """
    Create dict which keys is alphabetic characters. And values their number in alphabet
    Notes You could see an implementaion of this one in test, but create another one
    Examples:
        alphabet()
        >>> {"a": 1, "b": 2 ...}
    """
    pass


def simple_sort(lis):

    lis = lis.sort()
    """
    Sort list of ints without using built-in methods.
    Examples:
        simple_sort([2, 9, 6, 7, 3, 2, 1])
        >>> [1, 2, 2, 3, 6, 7, 9]
    Returns:

    """
    pass
