import random
import string
from typing import List, Dict, Union, Generator

# We will work with such dicts
ST = Dict[str, Union[str, int]]
# And we will put this dicts in list
DT = List[ST]


def task_1_fix_names_start_letter(data: DT) -> DT:
    """
    Make all `names` field in list of students to start from upper letter

    Examples:
        fix_names_start_letters([{'name': 'Alex', 'age': 26}, {'name': 'denys', 'age': 89}])
        >>> [{'name': 'Alex', 'age': 26}, {'name': 'Denys', 'age': 89}]
    """
    i = 0
    for lis in data:
        for key, values in lis.items():
            if key == 'name':
                lis[key] = values.capitalize()
        data[i] = lis
        i = i + 1

    return data


def task_2_remove_dict_fields(data: DT, redundant_keys: List[str]) -> DT:
    """given_data
    Remove from dictionaries given key value

    Examples:
       remove_dict_field([{'name': 'Alex', 'age': 26}, {'name': 'denys', 'age': 89}], 'age')
        >>> [{'name': 'Alex'}, {'name': 'denys'}]
    """
    new_data = list()
    redundant_keys = list()
    for element in data:
        elements = {key: value for key, value in element.items() if key not in redundant_keys}
        new_data.append(elements)
    return new_data


def task_3_find_item_via_value(data: DT, value) -> DT:
    """
    Find and return all items that has @searching value in any key
    Examples:
        find_item_via_value([{'name': 'Alex', 'age': 26}, {'name': 'denys', 'age': 89}], 26)
        >>> [{'name': 'Alex', 'age': 26}]
    """
    new_data = list()
    value_to_search = value
    for element in data:
        elements = {key: value for value, key in element.items() if value == value_to_search}
        new_data.append(elements)
    return new_data


def task_4_min_value_integers(data: List[int]) -> int:
    """
    Find and return minimum value from list
    """
    try:
        return min(data)
    except ValueError:
        pass


def task_5_min_value_strings(data: List[Union[str, int]]) -> str:
    """
    Find the longest string
    """
    try:
        return str(min(data, key=lambda i: len(str(i))))
    except ValueError:
        pass


def task_6_min_value_list_of_dicts(data: DT, key: str) -> ST:
    """
    Find minimum value by given key
    Returns:

    """
    a = []
    for i in data:
        if key in i.keys():
            a.append(i[key])
    return min(a)


def task_7_max_value_list_of_lists(data: List[List[int]]) -> int:
    """
    Find max value from list of lists
    """
    new = []
    for elements in data:
        new.append(max(elements))
    return max(new)


def task_8_sum_of_ints(data: List[int]) -> int:
    """
    Find sum of all items in given list
    """
    sum_of = int()
    for element in data:
        sum_of = sum_of + element
    return sum_of


def task_9_sum_characters_positions(text: str) -> int:
    """
    Please read first about ascii table.
    https://python-reference.readthedocs.io/en/latest/docs/str/ASCII.html
    You need to calculate sum of decimal value of each symbol in text

    Examples:
        task_9_sum_characters_positions("A")
        >>> 65
        task_9_sum_characters_positions("hello")
        >>> 532
    """
    return sum(ord(i) for i in text)


def task_10_generator_of_simple_numbers() -> Generator[int, None, None]:
    """
    Return generator of simple numbers
    Stop then iteration if returned value is more than 200
    Examples:
        a = task_10_generator_of_simple_numbers()
        next(a)
        >>> 2
        next(a)
        >>> 3
    """
    pass


def task_11_create_list_of_random_characters() -> List[str]:
    """
    Create list of 20 elements where each element is random letter from latin alphabet

    """
    lis = []
    while len(lis) <= 19:
        lis.append(random.choice(string.ascii_lowercase))
    return lis
