#!/usr/bin/python3

if __name__ == "__main__":
    """
    This script calculates and prints the sum of 1 and 2.

    It imports the 'add' function from the 'add_0' module to perform the addition.

    The values 1 and 2 are assigned to variables 'a' and 'b', respectively.
    The result of the addition is then printed using a formatted string.

    Note: This script assumes the 'add_0' module is available in the same directory.
    """
    from add_0 import add

    a = 1
    b = 2
    print("{} + {} = {}".format(a, b, add(a, b)))
