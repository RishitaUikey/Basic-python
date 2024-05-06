'''Write a Python program to get a list with n elements removed from the left and right.
Sample Output:
Original list elements:
[1, 2, 3]
Remove 1 element from left of the said list:
[2, 3]
Remove 1 element from right of the said list:
[1, 2]
Original list elements:
[1, 2, 3, 4]
Remove 2 elements from left of the said list:
[3, 4]
Remove 2 elements from right of the said list:
[1, 2]
Original list elements:
[1, 2, 3, 4, 5, 6]
Remove 7 elements from left of the said list:
[2, 3, 4, 5, 6]
Remove 7 elements from right of the said list:
[1, 2, 3, 4, 5]'''

def remove_elements(lst, n_left, n_right):
    return lst[n_left:len(lst) - n_right]

sample_lists = [
    [1, 2, 3],
    [1, 2, 3, 4],
    [1, 2, 3, 4, 5, 6]
]
sample_values = [
    (1, 1),
    (2, 2),
    (7, 7)
]

for lst, (n_left, n_right) in zip(sample_lists, sample_values):
    print("Original list elements:")
    print(lst)
    if n_left > 0:
        print(f"Remove {n_left} element{'s' if n_left > 1 else ''} from left of the said list:")
        print(remove_elements(lst, n_left, 0))
    if n_right > 0:
        print(f"Remove {n_right} element{'s' if n_right > 1 else ''} from right of the said list:")
        print(remove_elements(lst, 0, n_right))

