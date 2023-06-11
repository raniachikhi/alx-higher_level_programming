#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new = []
    for n in my_list:
        if (n % 2) == 0:
            new.append(True)
        else:
            new.append(False)
    return(new)
