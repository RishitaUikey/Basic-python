'''Write a  Python program to move the specified number of elements to the end of the given list.
Sample Output:
[4, 5, 6, 7, 8, 1, 2, 3]
[6, 7, 8, 1, 2, 3, 4, 5]
[1, 2, 3, 4, 5, 6, 7, 8]
[1, 2, 3, 4, 5, 6, 7, 8]
[8, 1, 2, 3, 4, 5, 6, 7]
[2, 3, 4, 5, 6, 7, 8, 1]'''

def move_elements_to_end(lst, n):
    return lst[n:] + lst[:n]

sample_lists = [
    [1, 2, 3, 4, 5, 6, 7, 8],
    [1, 2, 3, 4, 5, 6, 7, 8],
    [1, 2, 3, 4, 5, 6, 7, 8],
    [1, 2, 3, 4, 5, 6, 7, 8],
    [1, 2, 3, 4, 5, 6, 7, 8],
    [1, 2, 3, 4, 5, 6, 7, 8]
]

n_values = [3, 5, 0, 8, 1, 2]
for lst, n in zip(sample_lists, n_values):
    print(move_elements_to_end(lst, n))
