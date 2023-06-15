#!/usr/bin/python3
def roman_to_int(roman_string):
    roman_values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    previous_value = 0

    if isinstance(roman_string, str) and roman_string:
        for index in range(len(roman_string) - 1, -1, -1):
            current_value = roman_values[roman_string[index]]
            if current_value >= previous_value:
                result += current_value
            else:
                result -= current_value
            previous_value = current_value
    return result
