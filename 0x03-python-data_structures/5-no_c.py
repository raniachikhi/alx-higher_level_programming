#!/usr/bin/python3
def no_c(my_string):
    l_chars = list(my_string)
    for c in l_chars:
        if c == 'c' or c == 'C':
            l_chars.remove(c)
    return("".join(l_chars))
