#!/usr/bin/python3

import random

# Generate a random number between -10,000 and 10,000
number = random.randint(-10000, 10000)

# Extract the last digit of the number
digit = abs(number) % 10

# Adjust the sign of the digit if the number is negative
if number < 0:
    digit = -digit

# Print the number and the value of the last digit
print("Last digit of {} is {} and is ".format(number, digit), end="")

# Check the value of the digit and print the corresponding message
if digit > 5:
    print("greater than 5")
elif digit == 0:
    print("0")
else:
    print("less than 6 and not 0")
