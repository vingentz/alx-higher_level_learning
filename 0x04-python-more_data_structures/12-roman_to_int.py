#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or type(roman_string) is not str:
        return 0
    if roman_string == "":
        return 0
    num = 0
    romandic = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    for k, l in zip(roman_string, roman_string[1:]):
        if k not in romandic.keys():
            return 0
        elif romandic[k] >= romandic[l]:
            num += romandic[k]
        else:
            num -= romandic[k]
    num += romandic[roman_string[-1]]
    return num
