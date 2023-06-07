#!/usr/bin/python3
# 7-islower.py

def islower(c):
    """Check if a character is lowercase."""
    # Check if the character's ASCII value falls within
# the range of lowercase letters
    if ord(c) >= 97 and ord(c) <= 122:
        return True
    else:
        return False
