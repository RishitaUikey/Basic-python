'''Write a Python program to remove all characters except a specified character from a given string.
Original string
Python Exercises
Remove all characters except P in the said string:
P
Original string
google
Remove all characters except g in the said string:
gg
Original string
exercises
Remove all characters except e in the said string:
eee'''

def remove_except_char(input_string, char):
    result = ""
    for ch in input_string:
        if ch == char:
            result += ch
    return result
original_string1 = "Python Exercises"
specified_char1 = "P"
result1 = remove_except_char(original_string1, specified_char1)
print("Original string:", original_string1)
print("Remove all characters except", specified_char1, "in the said string:", result1)

original_string2 = "google"
specified_char2 = "g"
result2 = remove_except_char(original_string2, specified_char2)
print("Original string:", original_string2)
print("Remove all characters except", specified_char2, "in the said string:", result2)

original_string3 = "exercises"
specified_char3 = "e"
result3 = remove_except_char(original_string3, specified_char3)
print("Original string:", original_string3)
print("Remove all characters except", specified_char3, "in the said string:", result3)
