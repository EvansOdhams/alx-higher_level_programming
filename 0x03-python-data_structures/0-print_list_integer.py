#!/usr/bin/python3
# 0-print_list_integer.py


def print_list_integer(my_list=[]):
    """
    Prints all integers of a list.

    Args:
        my_list (list): List of integers.

    Returns:
        None
    """
    for i in my_list:
        print("{:d}".format(i))
