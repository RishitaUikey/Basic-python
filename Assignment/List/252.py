'''Write a Python program to get the n maximum elements from a given list of numbers.
Sample Output:
Original list elements:
[1, 2, 3]
Maximum values of the said list: [3]
Original list elements:
[1, 2, 3]
Two maximum values of the said list: [3, 2]
Original list elements:
[-2, -3, -1, -2, -4, 0, -5]
Threee maximum values of the said list: [0, -1, -2]
Original list elements:
[2.2, 2, 3.2, 4.5, 4.6, 5.2, 2.9]
Two maximum values of the said list: [5.2, 4.6]'''

def get_n_maximum_elements(lst, n):
    sorted_list = sorted(lst, reverse=True)
    return sorted_list[:n]

sample_lists = [
    [1, 2, 3],
    [1, 2, 3],
    [-2, -3, -1, -2, -4, 0, -5],
    [2.2, 2, 3.2, 4.5, 4.6, 5.2, 2.9]
]

sample_ns = [1, 2, 3, 2]

for lst, n in zip(sample_lists, sample_ns):
    print("Original list elements:")
    print(lst)
    print(f"{n} maximum values of the said list:", get_n_maximum_elements(lst, n))

