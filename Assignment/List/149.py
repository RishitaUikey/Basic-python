''' Write a Python program to get all possible combinations of the elements of a given list.
Original list:
['orange', 'red', 'green', 'blue']
All possible combinations of the said list's elements:
[[], ['orange'], ['red'], ['red', 'orange'], ['green'], ['green', 'orange'], ['green', 'red'], ['green', 'red', 'orange'], ['blue'], ['blue', 'orange'], ['blue', 'red'], ['blue', 'red', 'orange'], ['blue', 'green'], ['blue', 'green', 'orange'], ['blue', 'green', 'red'], ['blue', 'green', 'red', 'orange']]'''

from itertools import combinations

def get_all_combinations(input_list):
    all_combinations = []
    for r in range(len(input_list) + 1):
        all_combinations.extend(combinations(input_list, r))
    return all_combinations

original_list = ['orange', 'red', 'green', 'blue']
print("Original list:")
print(original_list)
print("All possible combinations of the said list's elements:")
print(get_all_combinations(original_list))
