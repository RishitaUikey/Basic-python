'''Write a  Python program to merge two or more lists into a list of lists, combining elements from each of the input lists based on their positions.
Sample Output:
After merging lists into a list of lists:
[['a', 1, True], ['b', 2, False]]
[['a', 1, True], [None, 2, False]]
[['a', 1, True], ['_', 2, False]]'''

def merge_lists(*lists):
    max_length = max(len(lst) for lst in lists)
    merged = [[lst[i] if i < len(lst) else None for lst in lists] for i in range(max_length)]
    return merged

list1 = ['a', 'b']
list2 = [1, 2]
list3 = [True, False]

print("After merging lists into a list of lists:")
print(merge_lists(list1, list2, list3))
