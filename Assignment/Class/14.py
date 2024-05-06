# Write a Python class to convert a Roman numeral to an integer.

class RomanToInteger:
    def __init__(self):
        self.numeral_map = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
        }

    def to_integer(self, roman):
        result = 0
        prev_value = 0
        for char in roman[::-1]:
            value = self.numeral_map[char]
            if value < prev_value:
                result -= value
            else:
                result += value
            prev_value = value
        return result

converter = RomanToInteger()
roman_numeral = 'CCXLVI'
print(f"The integer representation of {roman_numeral} is: {converter.to_integer(roman_numeral)}")
