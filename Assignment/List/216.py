''' Write a  Python program to group the elements of a list based on the given function and return the count of elements in each group.
Sample Output:
{6: 2, 4: 1}
{3: 2, 5: 1}'''

def group_elements(lst, func):
    groups = {}
    for item in lst:
        key = func(item)
        groups[key] = groups.get(key, 0) + 1
    return groups

sample_list1 = [6, 4, 6]
sample_list2 = [3, 5, 3]

print(group_elements(sample_list1, lambda x: x))
print(group_elements(sample_list2, lambda x: x))
