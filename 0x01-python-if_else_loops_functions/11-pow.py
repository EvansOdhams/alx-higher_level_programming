#!/usr/bin/python3
# 11-pow.py

def pow(a, b):
    result = 1
    for i in range(abs(b)):
        result *= a
    if b < 0:
        result = 1 / result
    return result
