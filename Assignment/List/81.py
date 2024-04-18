'''Write a  Python program to extract a given number of randomly selected elements from a given list.
Original list:
[1, 1, 2, 3, 4, 4, 5, 1]
Selected 3 random numbers of the above list:
[4, 4, 1]'''

import random

def select_random_elements(input_list, num_elements):
    return random.sample(input_list, num_elements)
original_list = [1, 1, 2, 3, 4, 4, 5, 1]
num_selected = 3
selected_elements = select_random_elements(original_list, num_selected)

print("Original list:")
print(original_list)
print("Selected {} random numbers of the above list:".format(num_selected))
print(selected_elements)
