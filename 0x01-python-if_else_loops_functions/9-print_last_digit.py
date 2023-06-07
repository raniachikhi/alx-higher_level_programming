#!/usr/bin/python3
# 9-print_last_digit.py

def print_last_digit(number):
    """Print the last digit of a number and return it."""
    # Calculate the absolute value of the number and find the remainder when divided by 10
    last_digit = abs(number) % 10
    # Print the last digit without a newline character
    print(last_digit, end="")
    # Return the last digit
    return last_digit
