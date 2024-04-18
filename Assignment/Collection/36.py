''' Write a  Python program to compare two unordered lists (not sets).
Sample Output:
False'''

def compare_lists(list1, list2):
    l1 = sorted(list1)
    l2 = sorted(list2)

    return l1 == l2

list1 = [3, 2, 1]
list2 = [1, 2, 3]

result = compare_lists(list1, list2)
print(result)
