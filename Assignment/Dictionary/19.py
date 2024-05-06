'''Write a Python program to combine two dictionary by adding values for common keys.
d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
Sample output: Counter({'a': 400, 'b': 400, 'd': 400, 'c': 300})'''

from collections import Counter

def combine_dicts(d1, d2):
    counter1 = Counter(d1)
    counter2 = Counter(d2)
    
    combined_counter = counter1 + counter2
    
    return combined_counter

d1 = {'a': 100, 'b': 200, 'c': 300}
d2 = {'a': 300, 'b': 200, 'd': 400}

combined_dict = combine_dicts(d1, d2)
print("Combined dictionary:", combined_dict)
