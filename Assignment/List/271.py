'''Write a Python program to check if there are duplicate values in a given flat list.
Sample Output:
Original list:
[1, 2, 3, 4, 5, 6, 7]
Check if there are duplicate values in the said given flat list:
False
Original list:
[1, 2, 3, 3, 4, 5, 5, 6, 7]
Check if there are duplicate values in the said given flat list:
True'''

def has_duplicates(lst):
    return len(lst) != len(set(lst))

sample_lists = [
    [1, 2, 3, 4, 5, 6, 7],
    [1, 2, 3, 3, 4, 5, 5, 6, 7]
]
for lst in sample_lists:
    print("Original list:")
    print(lst)
    print("Check if there are duplicate values in the said given flat list:")
    print(has_duplicates(lst))


