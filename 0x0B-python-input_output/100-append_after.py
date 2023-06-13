#!/usr/bin/python3
"""Define Class"""


def append_after(filename="", search_string="", new_string=""):
    """
    Inserts a line of text to a file after each line containing .

    Args:
        filename (str): The name of the file.
        search_string (str): The string to search for.
        new_string (str): The string to insert.

    Returns:
        None
    """
    with open(filename, 'r+', encoding='utf-8') as file:
        lines = file.readlines()
        file.seek(0)

        for line in lines:
            file.write(line)
            if search_string in line:
                file.write(new_string)

        file.truncate()
