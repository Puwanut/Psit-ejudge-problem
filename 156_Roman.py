"""Roman"""
def roman2dec(roman):
    """change roman number to decimal number"""
    roman_value = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    value_before = 9999
    total_value = 0
    for symbol in roman:
        value = roman_value[symbol]
        if value > value_before:
            total_value -= 2*value_before
        total_value += value
        value_before = value
    print(total_value)
roman2dec(input())
