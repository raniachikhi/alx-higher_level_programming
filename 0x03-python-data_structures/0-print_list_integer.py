#!/usr/bin/python3
#0-print_list_integer.py

def print_list_integer(my_list=[]):
    """takes a list of int & prints int on separate line"""
    for i in range(len(my_list)):
        print("{:d}".format(my_list[i]))
