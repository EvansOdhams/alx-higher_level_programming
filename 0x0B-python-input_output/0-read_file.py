#!/usr/bin/python3

def read_file(filename=""):
    """Reads a text file (UTF-8 encoded) and prints its content to stdout."""
    with open(filename, "r", encoding="UTF-8") as f:
        print(f.read(), end="")
