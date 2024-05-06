'''Write a  Python program to count the frequency of a dictionary.
Original Dictionary:
{'V': 10, 'VI': 10, 'VII': 40, 'VIII': 20, 'IX': 70, 'X': 80, 'XI': 40, 'XII': 20}
Count the frequency of the said dictionary:
Counter({10: 2, 40: 2, 20: 2, 70: 1, 80: 1})'''

from collections import Counter

def count_frequency(dictionary):
    values = dictionary.values()
    frequency = Counter(values)
    
    return frequency
original_dict = {'V': 10, 'VI': 10, 'VII': 40, 'VIII': 20, 'IX': 70, 'X': 80, 'XI': 40, 'XII': 20}

result = count_frequency(original_dict)
print("Count the frequency of the said dictionary:")
print(result)
