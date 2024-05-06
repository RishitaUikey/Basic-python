'''Write a Python program to find missing and additional values in two lists.
Sample data : Missing values in second list: b,a,c
Additional values in second list: g,h'''

def find_missing_and_additional(list1, list2):
    set1 = set(list1)
    set2 = set(list2)

    missing_values = sorted(list(set1 - set2))
    additional_values = sorted(list(set2 - set1))

    return missing_values, additional_values
list1 = ['a', 'b', 'c', 'd', 'e']
list2 = ['a', 'c', 'd', 'e', 'g', 'h']

missing, additional = find_missing_and_additional(list1, list2)
print("Missing values in the second list:", ', '.join(missing))
print("Additional values in the second list:", ', '.join(additional))
