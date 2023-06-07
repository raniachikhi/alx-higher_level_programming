#!/usr/bin/python3

# Print numbers from 0 to 99 in a two-digit format with
# leading zeros if necessary
# The numbers are separated by commas, except for the last
# number, 99
for i in range(100):
    if i < 10:
        print("0{}".format(i), end="")
    elif i == 99:
        print(i)
    else:
        print(i, end=", ")
