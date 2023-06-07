#!/usr/bin/python3

# Print the lowercase alphabet, excluding 'q' and 'e', without a newline character at the end
for letter in range(97, 123):
    if chr(letter) != 'q' and chr(letter) != 'e':
        print("{}".format(chr(letter)), end="")
