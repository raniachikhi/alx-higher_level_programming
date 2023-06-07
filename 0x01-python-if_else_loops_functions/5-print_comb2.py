#!/usr/bin/python3

# Print numbers from 0 to 99 in a two-digit format with
# leading zeros if necessary
# The numbers are separated by commas, except for the last
# number, 99
for i in range(0, 100):
    if i == 99:
        print(i)
    else:
        print("{:0>2d}".format(i), end=", ")
