#!/usr/bin/python3
"""
File name: 4-write_file.py
"""


def write_file(filename="", text=""):
    """
    write_file writes a string to a text file (UTF8) and
    returns the number of characters written.

    Args:
        filename (str): Name of the file. Defaults to "".
        text (str): Text to write. Defaults to "".

    Returns:
        int: Number of characters written.
    """
    with open(filename, 'w', encoding='utf-8') as file:
        return file.write(text)
