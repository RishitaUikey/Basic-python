'''Write a  Python program to count the number of non-empty substrings of a given string.'''

def count_non_empty_substrings(input_string):
    n = len(input_string)
    return int(n * (n + 1) / 2)
input_string = "abcd"
result = count_non_empty_substrings(input_string)
print("Number of non-empty substrings:", result)
