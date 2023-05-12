#!/usr/bin/python3
# 2-replace_in_list.py


def replace_in_list(my_list, idx, element):
    """
    Replaces an element of a list at a specific position

    Args:
        my_list (list): The list to modify
        idx (int): The index of the element to replace
        element (int): The element to use as replacement

    Returns:
        list: The modified list or the original list if the index is invalid
    """
    if idx < 0 or idx >= len(my_list):
        return my_list

    my_list[idx] = element
    return my_list
