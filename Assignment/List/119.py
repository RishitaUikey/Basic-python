'''Write a  Python program to check if a substring appears in a given list of string values.
Original list:
['red', 'black', 'white', 'green', 'orange']
Substring to search:
ack
Check if a substring presents in the said list of string values:
True
Substring to search:
abc
Check if a substring presents in the said list of string values:
False'''

def check_substring(lst, substring):
    for string in lst:
        if substring in string:
            return True
    return False

original_list = ['red', 'black', 'white', 'green', 'orange']

substring1 = 'ack'
substring2 = 'abc'

result1 = check_substring(original_list, substring1)
result2 = check_substring(original_list, substring2)

print("Original list:")
print(original_list)
print("Substring to search:")
print(substring1)
print("Check if a substring is present in the said list of string values:")
print(result1)
print("Substring to search:")
print(substring2)
print("Check if a substring is present in the said list of string values:")
print(result2)
