'''Write a  Python program to find the largest odd number in a given list of integers.
Sample Data:
([0, 9, 2, 4, 5, 6]) -> 9
([-4, 0, 6, 1, 0, 2]) -> 1
([1, 2, 3]) -> 3
([-4, 0, 5, 1, 0, 1]) -> 5'''

def largest_odd_number(lst):
    odd_numbers = [num for num in lst if num % 2 != 0]
    if odd_numbers:
        return max(odd_numbers)
    else:
        return None

sample_data = [
    [0, 9, 2, 4, 5, 6],
    [-4, 0, 6, 1, 0, 2],
    [1, 2, 3],
    [-4, 0, 5, 1, 0, 1]
]

for lst in sample_data:
    print(largest_odd_number(lst))