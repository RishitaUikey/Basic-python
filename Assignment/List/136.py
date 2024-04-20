'''Write a  Python program to remove duplicate words from a given list of strings.
Original String:
['Python', 'Exercises', 'Practice', 'Solution', 'Exercises']
After removing duplicate words from the said list of strings:
['Python', 'Exercises', 'Practice', 'Solution']'''

def remove_duplicate_words(lst):
    return list(set(lst))

original_list = ['Python', 'Exercises', 'Practice', 'Solution', 'Exercises']
result = remove_duplicate_words(original_list)
print("After removing duplicate words from the said list of strings:")
print(result)
