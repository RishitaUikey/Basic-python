'''Write a  Python program to sort a given list of tuples by a specified element.
Original list of tuples:
[('item2', 10, 10.12), ('item3', 15, 25.1), ('item1', 11, 24.5), ('item4', 12, 22.5)]
Sort on 1st element of the tuple of the said list:
[('item1', 11, 24.5), ('item2', 10, 10.12), ('item3', 15, 25.1), ('item4', 12, 22.5)]
Sort on 2nd element of the tuple of the said list:
[('item2', 10, 10.12), ('item1', 11, 24.5), ('item4', 12, 22.5), ('item3', 15, 25.1)]
Sort on 3rd element of the tuple of the said list:
[('item2', 10, 10.12), ('item4', 12, 22.5), ('item1', 11, 24.5), ('item3', 15, 25.1)]'''

def sort_tuples(lst, element_index):
    return sorted(lst, key=lambda x: x[element_index])
original_list = [('item2', 10, 10.12), ('item3', 15, 25.1), ('item1', 11, 24.5), ('item4', 12, 22.5)]
print("Original list of tuples:")
print(original_list)
print("\nSort on 1st element of the tuple of the said list:")
print(sort_tuples(original_list, 0))
print("\nSort on 2nd element of the tuple of the said list:")
print(sort_tuples(original_list, 1))
print("\nSort on 3rd element of the tuple of the said list:")
print(sort_tuples(original_list, 2))
