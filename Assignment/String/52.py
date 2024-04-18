'''Write a Python program to print all permutations with a given 
repetition number of characters of a given string.'''

from itertools import product

def permutations_with_repetition(string, repetition):
    perm_with_rep = product(string, repeat=repetition)
    for perm in perm_with_rep:
        print(''.join(perm))
input_string = input("Enter a string: ")
repetition = int(input("Enter the repetition number: "))

print("Permutations with repetition:")
permutations_with_repetition(input_string, repetition)
