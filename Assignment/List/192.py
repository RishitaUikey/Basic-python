'''Write a  Python program to remove all strings from a given list of tuples.
Original list:
[(100, 'Math'), (80, 'Math'), (90, 'Math'), (88, 'Science', 89), (90, 'Science', 92)]
Remove all strings from the said list of tuples:
[(100,), (80,), (90,), (88, 89), (90, 92)]'''

def remove_strings_from_tuples(lst):
    result = []
    for tup in lst:
        new_tup = tuple(item for item in tup if not isinstance(item, str))
        result.append(new_tup)
    return result

original_list = [(100, 'Math'), (80, 'Math'), (90, 'Math'), (88, 'Science', 89), (90, 'Science', 92)]
result_list = remove_strings_from_tuples(original_list)
print("Original list:")
print(original_list)
print("Remove all strings from the said list of tuples:")
print(result_list)
