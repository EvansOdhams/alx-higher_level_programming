#!/usr/bin/python3
"""
Module that defines a class MyList
"""


class MyList(list):
    """
    Custom class that inherits from list
    """

    def print_sorted(self):
        """
        Prints the list in sorted order (ascending sort)
        """
        sorted_list = sorted(self)
        print(sorted_list)
