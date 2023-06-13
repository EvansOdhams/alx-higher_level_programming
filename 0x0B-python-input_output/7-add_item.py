#!/usr/bin/python3
import sys
import json


def add_item(filename, *args):
    """
    Add items to a JSON file.

    Args:
        filename (str): The name of the JSON file.
        *args: Variable number of items to add.

    Returns:
        None
    """
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            items = json.load(file)
    except FileNotFoundError:
        items = []

    items.extend(args)

    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(items, file)


# Testing the code
if __name__ == "__main__":
    filename = 'add_item.json'
    add_item(filename, *sys.argv[1:])
