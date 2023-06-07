#!/usr/bin/python3
# 8-uppercase.py

def uppercase(str):
    # Iterate over each character in the string
    for c in str:
        # Check if the character is lowercase and convert it to uppercase
        if ord(c) >= 97 and ord(c) <= 122:
            c = chr(ord(c) - 32)
        # Print the character
        print("{}".format(c), end="")
    # Print a newline character to separate the output
    print("")
