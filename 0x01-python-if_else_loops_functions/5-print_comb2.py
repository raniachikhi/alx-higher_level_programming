#!/usr/bin/python3

# Print numbers from 0 to 99 in a two-digit format with leading
# zeros if necessary
# The numbers are separated by commas, except for the last
# number, 99
for number in range(0, 100):
    if number == 99:
        print("{}".format(number))
    else:
        print("{:02}".format(number), end=", ")
