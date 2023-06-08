#!/usr/bin/python3

if __name__ == "__main__":
''''The values 1 and 2 are assigned to variables 'a' and 'b', respectively. The sum of 'a' and 'b'
is then printed using a formatted string.'''
    from add_0 import add

    a = 1
    b = 2
    print("{} + {} = {}".format(a, b, add(a, b)))
