'''Write a  Python program to get the n minimum elements from a given list of numbers.
Sample Output:
Original list elements:
[1, 2, 3]
Minimum values of the said list: [1]
Original list elements:
[1, 2, 3]
Two minimum values of the said list: [1, 2]
Original list elements:
[-2, -3, -1, -2, -4, 0, -5]
Threee minimum values of the said list: [-5, -4, -3]
Original list elements:
[2.2, 2, 3.2, 4.5, 4.6, 5.2, 2.9]
Two minimum values of the said list: [2, 2.2]'''

def get_n_minimum_elements(lst, n):
    sorted_list = sorted(lst)
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
    print(f"{n} minimum values of the said list:", get_n_minimum_elements(lst, n))

