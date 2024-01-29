#!/usr/bin/python3
def roman_to_int(roman_string):
    result = 0
    nr = {"I": 1, "V": 5, 
                     "X": 10, "L": 50, 
                     "C": 100, "D": 500, 
                     "M": 1000}
    if type(roman_string) != str:
        return 0
    if roman_string is None:
        return 0
    for idx in range(len(roman_string)):
        if idx > 0 and nr[roman_string[idx]] > nr[roman_string[idx - 1]]:
            result += nr[roman_string[idx]] - 2 * nr[roman_string[idx - 1]]
        else:
            result += nr[roman_string[idx]]
    return result
