'''Write a Python program to count the number of substrings with the
same first and last characters in a given string.'''

def count_substrings_same_first_last(input_string):
    count = 0
    for i in range(len(input_string)):
        for j in range(i, len(input_string)):
            if input_string[i] == input_string[j]:
                count += 1
    return count
input_string = "abca"
result = count_substrings_same_first_last(input_string)
print("Number of substrings with the same first and last characters:", result)
