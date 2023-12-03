#!/usr/bin/python3

def find_peak(list_of_integers):
    if not list_of_integers:
        return None  # Return None for an empty list
    
    low, high = 0, len(list_of_integers) - 1

    while low < high:
        mid = (low + high) // 2

        if list_of_integers[mid] > list_of_integers[mid + 1]:
            high = mid  # The peak is likely on the left side
        else:
            low = mid + 1  # The peak is likely on the right side or at mid

    return list_of_integers[low]
