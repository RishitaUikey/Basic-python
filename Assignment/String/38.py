'''Write a Python program to count occurrences of a substring in a string.'''
def count_substring_occurrences(string, substring):
    count = string.count(substring)
    return count

string = "hi everyone, hello everyone"
substring = "everyone"
occurrences = count_substring_occurrences(string, substring)
print("Occurrences of '{}' in '{}': {}".format(substring, string, occurrences))
