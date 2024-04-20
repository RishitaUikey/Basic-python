'''Write a Python program to sum the missing numbers in a given list of integers.
Sample Data:
([0, 3, 4, 7, 9]) -> 22
([44, 45, 48]) -> 93
([-7, -5, -4, 0]) -> -12'''

def sum_missing_numbers(lst):
    min_num = min(lst)
    max_num = max(lst)
    return sum(num for num in range(min_num, max_num) if num not in lst)
sample_data = [
    [0, 3, 4, 7, 9],
    [44, 45, 48],
    [-7, -5, -4, 0]
]

for lst in sample_data:
    print(sum_missing_numbers(lst))
