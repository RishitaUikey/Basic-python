'''Write a  Python program to sort one list based on another list containing the desired indexes.
Sample Output:
['apples', 'bread', 'eggs', 'jam', 'milk', 'oranges']
['oranges', 'milk', 'jam', 'eggs', 'bread', 'apples']'''

def sort_list_by_index(original_list, index_list):
    paired_lists = zip(original_list, index_list)
    sorted_pairs = sorted(paired_lists, key=lambda x: x[1])
    sorted_list = [pair[0] for pair in sorted_pairs]
    return sorted_list

original_list = ['apples', 'bread', 'eggs', 'jam', 'milk', 'oranges']
index_list = [5, 4, 3, 2, 1, 0]

print(original_list)
print(sort_list_by_index(original_list, index_list))
