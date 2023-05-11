#!/usr/bin/env python3

import sys
from calculator_1 import add, sub, mul, div

OPERATORS = {
    '+': add,
    '-': sub,
    '*': mul,
    '/': div,
}

def usage_and_exit():
    print('Usage: ./100-my_calculator.py <a> <operator> <b>')
    sys.exit(1)

def unknown_operator_and_exit():
    print('Unknown operator. Available operators: +, -, * and /')
    sys.exit(1)

if __name__ == '__main__':
    if len(sys.argv) != 4:
        usage_and_exit()

    a, operator, b = sys.argv[1:]
    if operator not in OPERATORS:
        unknown_operator_and_exit()

    try:
        a = int(a)
        b = int(b)
    except ValueError:
        usage_and_exit()

    result = OPERATORS[operator](a, b)
    print(f'{a} {operator} {b} = {result}')
