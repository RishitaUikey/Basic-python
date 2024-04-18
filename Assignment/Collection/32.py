'''Write a  Python program to find the class wise roll number from a tuple-of-tuples.
Sample Output:
defaultdict(<class 'list'>, {'V': [1, 2], 'VI': [1, 2, 3], 'VII': [1]})'''

from collections import defaultdict

def class_wise_roll_numbers(tuples):
    class_roll_numbers = defaultdict(list)
    for class_name, roll_numbers in tuples:
        class_roll_numbers[class_name].extend(roll_numbers)

    return class_roll_numbers

tuples_of_tuples = (('V', [1, 2]), ('VI', [1, 2, 3]), ('VII', [1]))
result = class_wise_roll_numbers(tuples_of_tuples)
print(result)

