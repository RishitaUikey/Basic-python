'''Write a  Python program to check if the elements of the first list are contained in the second one regardless of order.
Sample Output:
True
True
False
True'''

def are_elements_contained(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    return set1.issubset(set2)

sample_lists = [
    ([1, 2, 3], [1, 2, 3, 4, 5]),
    ([4, 2, 1], [1, 2, 3, 4, 5]),
    ([1, 2, 3], [4, 5, 6]),
    ([1], [1, 2, 3, 4])
]

for list1, list2 in sample_lists:
    print(are_elements_contained(list1, list2))

