#!/usr/bin/python3
# 11-delete_at.py


def delete_at(my_list=[], idx=0):
    if idx < 0 or idx >= len(my_list):
        return my_list
    else:
        return my_list[:idx] + my_list[idx+1:]
