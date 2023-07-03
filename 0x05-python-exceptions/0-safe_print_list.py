#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """Prints a specified number of elements from a list.

    Args:
        my_list (list): The list from which elements are printed. Defaults to an empty list if not provided.
        x (int): The number of elements to print from my_list. Defaults to 0 if not provided.

    Returns:
        int: The actual number of elements printed.
    """
    ret = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            ret += 1
        except IndexError:
            break
    print("")
    return (ret)
