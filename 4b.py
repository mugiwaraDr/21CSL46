def roman2dec(roman_str):
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    romanback = list(roman_str)[::-1]
    value = 0
    rightval = roman_dict[romanback[0]]
    for num in romanback:
        leftval = roman_dict[num]
        if leftval < rightval:
            value -= leftval
        else:
            value += leftval
        rightval = leftval

    return value


romanstr = input('enter astring')
print(roman2dec(romanstr))
