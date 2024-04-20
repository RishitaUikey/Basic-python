''' Write a  Python program to sort a given mixed list of integers and strings. Numbers must be sorted before strings.
Original list:
[19, 'red', 12, 'green', 'blue', 10, 'white', 'green', 1]
Sort the said mixed list of integers and strings:
[1, 10, 12, 19, 'blue', 'green', 'green', 'red', 'white']'''

def sort_mixed_list(lst):
    integers = [x for x in lst if isinstance(x, int)]
    strings = [x for x in lst if isinstance(x, str)]
    integers.sort()
    strings.sort()
    sorted_list = integers + strings
    return sorted_list

original_list = [19, 'red', 12, 'green', 'blue', 10, 'white', 'green', 1]
sorted_list = sort_mixed_list(original_list)
print("Sort the said mixed list of integers and strings:")
print(sorted_list)
