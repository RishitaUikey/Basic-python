'''Write a  Python program to find the specified number of maximum values in a given dictionary.
Original Dictionary:
{'a': 5, 'b': 14, 'c': 32, 'd': 35, 'e': 24, 'f': 100, 'g': 57, 'h': 8, 'i': 100}
1 maximum value(s) in the said dictionary:
['f']
2 maximum value(s) in the said dictionary:
['f', 'i']
5 maximum value(s) in the said dictionary:
['f', 'i', 'g', 'd', 'c']'''

import heapq

def find_max_values(dictionary, n):
    max_values = heapq.nlargest(n, dictionary, key=dictionary.get)
    return max_values

original_dict = {'a': 5, 'b': 14, 'c': 32, 'd': 35, 'e': 24, 'f': 100, 'g': 57, 'h': 8, 'i': 100}
n_values = [1, 2, 5]

for n in n_values:
    print(f"{n} maximum value(s) in the said dictionary:")
    print(find_max_values(original_dict, n))
