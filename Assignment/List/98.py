'''Write a  Python program to scramble the letters of a string in a given list.
Original list:
['Python', 'list', 'exercises', 'practice', 'solution']
After scrambling the letters of the strings of the said list:
['tnPhyo', 'tlis', 'ecrsseiex', 'ccpitear', 'noiltuos']'''

import random

def scramble_string_list(str_list):
    scrambled_list = [''.join(random.sample(word, len(word))) for word in str_list]
    return scrambled_list

original_list = ['Python', 'list', 'exercises', 'practice', 'solution']

scrambled_list = scramble_string_list(original_list)

print("Original list:")
print(original_list)
print("After scrambling the letters of the strings of the said list:")
print(scrambled_list)
