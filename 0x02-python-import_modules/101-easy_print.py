#!/usr/bin/python3

def magic_calculation(a, b):
    """Match bytecode provided by Holberton School."""
    if a < b:
        c = a + b
        for i in range(4, 6):
            c += i
        return c
    else:
        return a - b
