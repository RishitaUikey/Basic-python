# Write a Python program to shuffle and print a specified list.

import random

def shuffle_print_list(input_list):
    shuffled_list = input_list[:]
    random.shuffle(shuffled_list)
    print("Shuffled List:", shuffled_list)

example_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
shuffle_print_list(example_list)

