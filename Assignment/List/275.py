'''Write a  Python program to add all elements of a list of integers except the number at index. Return the updated string.
Sample Data:
([0, 9, 2, 4, 5, 6] -> [26, 17, 24, 22, 21, 20]
([-4, 0, 6, 1, 0, 2]) -> [9, 5, -1, 4, 5, 3]
([1, 2, 3]) -> [5, 4, 3]
([-4, 0, 5, 1, 0, 1]) -> [7, 3, -2, 2, 3, 2]'''

def add_except_index(lst, index):
    total_sum = sum(lst)
    return [total_sum - lst[i] if i != index else total_sum for i in range(len(lst))]

sample_data = [
    ([0, 9, 2, 4, 5, 6], 0),
    ([-4, 0, 6, 1, 0, 2], 3),
    ([1, 2, 3], 2),
    ([-4, 0, 5, 1, 0, 1], 5)
]

for lst, idx in sample_data:
    print(add_except_index(lst, idx))
