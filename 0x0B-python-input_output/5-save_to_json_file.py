#!/usr/bin/python3
# 7-save_to_json_file.py
# Carlos Barros <1543@holbertonschool.com>
""" File: 7-save_to_json_file.py
"""

import json


def save_to_json_file(my_obj, filename):
    """Writes an object to a JSON file.

    Args:
        my_obj (object): The object to write.
        filename (str): The name of the file.

    Returns:
        None
    """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)
