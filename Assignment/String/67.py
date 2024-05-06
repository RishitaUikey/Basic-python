'''Write a Python program to remove all consecutive duplicates of a given string.'''

def remove_consecutive_duplicates(input_string):
    result = ""
    for i in range(len(input_string)):
        if i == 0 or input_string[i] != input_string[i - 1]:
            result += input_string[i]
    return result
input_string = "aaabbbcccddeefffg"
result = remove_consecutive_duplicates(input_string)
print("String after removing consecutive duplicates:", result)
