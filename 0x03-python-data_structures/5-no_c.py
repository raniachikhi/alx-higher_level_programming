#!/usr/bin/python3
def no_c(my_string):
    l_chars = list(my_string)
    for i in l_chars:
        if i == 'c' or i == 'C':
            l_chars.remove(i)
    return("".join(l_chars))
