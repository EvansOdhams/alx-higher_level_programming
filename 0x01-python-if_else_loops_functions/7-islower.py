#!/usr/bin/python3
# 7-islower.py

def islower(c):
    """
    Returns True if c is lowercase
    Returns False otherwise
    """
    if ord(c) >= 97 and ord(c) <= 122:
        return True
    else:
        return False
