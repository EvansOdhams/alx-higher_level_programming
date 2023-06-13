#!/usr/bin/python3
# 2-append_write.py
# John Doe <johndoe@example.com>
""" File name: 2-append_write.py
"""


def append_write(filename="", text=""):
    """append_write appends a string at the end of a text file (UTF8) and
    returns the number of characters added.

    Args:
        filename (str): Name of the file. Defaults to "".
        text (str): Text to append. Defaults to "".

    Returns:
        int: Number of characters added.
    """
    with open(filename, 'a', encoding='utf-8') as file:
        return file.write(text)
