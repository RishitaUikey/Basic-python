'''Write a  Python program to create a two-dimensional list from a given list of lists.
Sample Output:
[(1, 4, 7, 10), (2, 5, 8, 11), (3, 6, 9, 12)]
[(1, 4), (2, 5)]'''

def transpose_lists(lists):
    return list(zip(*lists))

sample_lists = [
    [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]],
    [[1, 2], [4, 5]]
]
for lists in sample_lists:
    print(transpose_lists(lists))

