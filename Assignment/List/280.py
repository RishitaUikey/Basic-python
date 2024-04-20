'''Write a Python program that takes a list of integers and finds all pairs of integers that differ by three. Return all pairs of integers in a list.
Sample Data:
([0, 3, 4, 7, 9]) -> [[0, 3], [4, 7]]
[0, -3, -5, -7, -8] -> [[-3, 0], [-8, -5]]
([1, 2, 3, 4, 5]) -> [[1, 4], [2, 5]]
([100, 102, 103, 114, 115]) -> [[100, 103]]'''

def find_pairs(lst):
    pairs = []
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if abs(lst[i] - lst[j]) == 3:
                pairs.append([lst[i], lst[j]])
    return pairs

sample_data = [
    [0, 3, 4, 7, 9],
    [0, -3, -5, -7, -8],
    [1, 2, 3, 4, 5],
    [100, 102, 103, 114, 115]
]
for lst in sample_data:
    print(find_pairs(lst))
