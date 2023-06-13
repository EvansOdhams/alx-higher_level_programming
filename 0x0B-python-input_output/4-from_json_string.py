#!/usr/bin/python3
# 6-from_json_string.py
# Carlos Barros <1543@holbertonschool.com>
""" File: 6-from_json_string.py
"""

import json


def from_json_string(my_str):
    """Converts a JSON string representation to a Python data structure.

    Args:
        my_str (str): The JSON string to convert.

    Returns:
        object: The Python data structure representing the JSON string.
    """
    return json.loads(my_str)
