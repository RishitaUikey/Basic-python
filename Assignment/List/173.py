'''Write a  Python program to merge some list items in a given list using the index value.
Original lists:
['a', 'b', 'c', 'd', 'e', 'f', 'g']
Merge items from 2 to 4 in the said List:
['a', 'b', 'cd', 'e', 'f', 'g']
Merge items from 3 to 7 in the said List:
['a', 'b', 'c', 'defg']'''


def merge_list_items(lst, start, end):
    merged_item = ''.join(lst[start:end+1])
    return lst[:start] + [merged_item] + lst[end+1:]

original_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
result1 = merge_list_items(original_list, 2, 4)
print("Merge items from 2 to 4 in the said List:")
print(result1)
result2 = merge_list_items(original_list, 3, 7)
print("Merge items from 3 to 7 in the said List:")
print(result2)
