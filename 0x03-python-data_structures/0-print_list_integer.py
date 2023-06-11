#!/usr/bin/python3
#0-print_list_integer.py

def print_list_integer(my_list=[]):
    """takes a list of int & prints int on separate line"""
    if my_list is None:
        my_list = []
    for i in my_list:
        print(i)
