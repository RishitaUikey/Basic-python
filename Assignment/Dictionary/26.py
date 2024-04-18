'''Write a Python program to count the values associated with a key in a dictionary.
Expected Output:
6
2'''

def count_values(dictionary, key):
    total = sum(dictionary.get(k, 0) for k in dictionary.keys() if k == key)
    return total
sample_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 2, 'e': 1}
key_to_count = 'a'
result = count_values(sample_dict, key_to_count)
print(result)
