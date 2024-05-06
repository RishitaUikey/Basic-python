'''Write a  Python program to find the last occurrence of a specified item in a given list.
Original list:
['s', 'd', 'f', 's', 'd', 'f', 's', 'f', 'k', 'o', 'p', 'i', 'w', 'e', 'k', 'c']
Last occurrence of f in the said list:
7
Last occurrence of c in the said list:
15
Last occurrence of k in the said list:
14
Last occurrence of w in the said list:
12'''

def last_occurrence(lst, item):
    return len(lst) - 1 - lst[::-1].index(item)

original_list = ['s', 'd', 'f', 's', 'd', 'f', 's', 'f', 'k', 'o', 'p', 'i', 'w', 'e', 'k', 'c']
items_to_find = ['f', 'c', 'k', 'w']
for item in items_to_find:
    print(f"Last occurrence of {item} in the said list:")
    print(last_occurrence(original_list, item))
