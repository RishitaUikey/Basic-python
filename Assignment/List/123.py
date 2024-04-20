'''Write a  Python program to reverse strings in a given list of string values.
Original lists:
['Red', 'Green', 'Blue', 'White', 'Black']
Reverse strings of the said given list:
['deR', 'neerG', 'eulB', 'etihW', 'kcalB']'''

def reverse_strings(string_list):
    reversed_list = [string[::-1] for string in string_list]
    return reversed_list

string_list = ['Red', 'Green', 'Blue', 'White', 'Black']

reversed_list = reverse_strings(string_list)

print("Original lists:")
print(string_list)
print("Reverse strings of the said given list:")
print(reversed_list)
