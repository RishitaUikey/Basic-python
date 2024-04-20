'''Write a  Python program to randomize the order of the values of a list, returning a new list.
Sample Output:
Original list: [1, 2, 3, 4, 5, 6]
Shuffle the elements of the said list:
[3, 2, 4, 1, 6, 5]'''

import random

def shuffle_list(original_list):
    shuffled_list = original_list.copy()
    random.shuffle(shuffled_list)
    return shuffled_list

original_list = [1, 2, 3, 4, 5, 6]
print("Original list:", original_list)
print("Shuffle the elements of the said list:")
print(shuffle_list(original_list))
