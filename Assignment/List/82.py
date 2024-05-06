'''Write a Python program to generate combinations of n distinct objects taken from the elements of a given list.
Original list: [1, 2, 3, 4, 5, 6, 7, 8, 9] Combinations of 2 distinct objects: [1, 2] [1, 3] [1, 4] [1, 5] .... [7, 8] [7, 9] [8, 9]'''

from itertools import combinations

def generate_combinations(input_list, num_elements):
    return list(combinations(input_list, num_elements))

original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
num_elements = 2

combinations_list = generate_combinations(original_list, num_elements)

print("Original list:", original_list)
print("Combinations of {} distinct objects:".format(num_elements))
for combination in combinations_list:
    print(combination)
