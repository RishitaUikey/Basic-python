'''Write a  Python program to calculate the largest and smallest gap between sorted elements of a list of integers.
Sample Data:
{1, 2 ,9, 0, 4, 6} -> 3
{23, -2, 45, 38, 12, 4, 6} -> 15'''

def calculate_gaps(lst):
    sorted_lst = sorted(lst)
    gaps = [sorted_lst[i + 1] - sorted_lst[i] for i in range(len(sorted_lst) - 1)]
    largest_gap = max(gaps)
    smallest_gap = min(gaps)
    return largest_gap, smallest_gap

sample_data = [
    [1, 2, 9, 0, 4, 6],
    [23, -2, 45, 38, 12, 4, 6]
]
for lst in sample_data:
    largest_gap, smallest_gap = calculate_gaps(lst)
    print("Largest Gap:", largest_gap)
    print("Smallest Gap:", smallest_gap)

