#!/usr/bin/python3

"""
Import functions from calculator_1.py and print their results
"""

if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div

    # Define values for a and b
    a = 10
    b = 5

    # Print sum of a and b
    print("{} + {} = {}".format(a, b, add(a, b)))

    # Print difference of a and b
    print("{} - {} = {}".format(a, b, sub(a, b)))

    # Print product of a and b
    print("{} * {} = {}".format(a, b, mul(a, b)))

    # Print quotient of a and b
    print("{} / {} = {}".format(a, b, div(a, b))))
