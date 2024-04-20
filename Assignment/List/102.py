'''Write a  Python program to extract specified size of strings from a give list of string values.
Original list:
[' Python', 'list', 'exercises', 'practice', 'solution']
length of the string to extract:
8
After extracting strings of specified length from the said list:
['practice', 'solution']'''

def extract_strings_by_length(lst, length):
    return [string for string in lst if len(string.strip()) == length]
original_list = [' Python', 'list', 'exercises', 'practice', 'solution']
length_to_extract = 8
extracted_strings = extract_strings_by_length(original_list, length_to_extract)
print("length of the string to extract:",length_to_extract)
print("After extracting strings of specified length from the said list:",extracted_strings)