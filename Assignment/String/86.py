'''Write a  Python program to delete all occurrences of a specified character in a given string.
Sample Output:
Original string:
Delete all occurrences of a specified character in a given string
Modified string:
Delete ll occurrences of specified chrcter in given string'''
def delete_char(input_string, char):
    modified_string = input_string.replace(char, '')

    return modified_string
original_string = "Delete all occurrences of a specified character in a given string"
char_to_delete = 'a'

print("Original string:")
print(original_string)

modified_string = delete_char(original_string, char_to_delete)

print("Modified string:")
print(modified_string)
