#!/usr/bin/python3
def calculate_subtraction(subtraction_list):
    total_subtraction = 0
    max_value = max(subtraction_list)

    for num in subtraction_list:
        if max_value > num:
            total_subtraction += num

    return max_value - total_subtraction


def roman_to_int(roman_string):
    if not roman_string:
        return 0

    if not isinstance(roman_string, str):
        return 0

    roman_numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    numeral_keys = list(roman_numerals.keys())

    result = 0
    last_numeral = 0
    subtraction_list = [0]

    for char in roman_string:
        for numeral in numeral_keys:
            if numeral == char:
                if roman_numerals.get(char) <= last_numeral:
                    result += calculate_subtraction(subtraction_list)
                    subtraction_list = [roman_numerals.get(char)]
                else:
                    subtraction_list.append(roman_numerals.get(char))

                last_numeral = roman_numerals.get(char)

    result += calculate_subtraction(subtraction_list)

    return result
