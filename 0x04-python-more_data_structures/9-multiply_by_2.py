#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dictionary = a_dictionary.copy()
    list_of_keys = list(new_dictionary.keys())

    for k in list_of_keys:
        new_dictionary[k] *= 2

    return (new_dictionary)
