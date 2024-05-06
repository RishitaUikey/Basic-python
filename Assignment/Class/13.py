# Write a Python class to convert an integer to a Roman numeral.

class IntegerToRoman:
    def __init__(self):
        self.numeral_map = [
            (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
            (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
            (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
        ]

    def to_roman(self, num):
        result = ''
        for value, symbol in self.numeral_map:
            while num >= value:
                result += symbol
                num -= value
        return result

# Example usage:
converter = IntegerToRoman()
number = 354
print(f"The Roman numeral representation of {number} is: {converter.to_roman(number)}")
