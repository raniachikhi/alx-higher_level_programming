#!/usr/bin/python3
# 2-print_alphabet.py

# Print the alphabet in lowercase, without a newline character at the end
for letter in range(97, 123):
    print("{}".format(chr(letter)), end="")
