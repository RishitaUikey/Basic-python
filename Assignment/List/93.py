'''Write a  Python program to count the number of sublists that contain a particular element.
Original list:
[[1, 3], [5, 7], [1, 11], [1, 15, 7]]
Count 1 in the said list:
3
Count 7 in the said list:
2
Original list:
[['A', 'B'], ['A', 'C'], ['A', 'D', 'E'], ['B', 'C', 'D']]
Count 'A' in the said list:
3
Count 'E' in the said list:
1'''

def count_element_occurrences(lst, element):
    count = sum(1 for sublist in lst if element in sublist)
    return count

lists1 = [[1, 3], [5, 7], [1, 11], [1, 15, 7]]
lists2 = [['A', 'B'], ['A', 'C'], ['A', 'D', 'E'], ['B', 'C', 'D']]

count_1 = count_element_occurrences(lists1, 1)
count_7 = count_element_occurrences(lists1, 7)
count_A = count_element_occurrences(lists2, 'A')
count_E = count_element_occurrences(lists2, 'E')

print("Original list:")
print(lists1)
print(f"Count 1 in the said list: {count_1}")
print(f"Count 7 in the said list: {count_7}")

print("\nOriginal list:")
print(lists2)
print(f"Count 'A' in the said list: {count_A}")
print(f"Count 'E' in the said list: {count_E}")
