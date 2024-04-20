''' Write a Python program to calculate the difference between two iterables, without filtering duplicate values.
Sample Output:
[3]'''

def calculate_difference(iterable1, iterable2):
    set1 = set(iterable1)
    set2 = set(iterable2)
    return list(set1.difference(set2))

iterable1 = [1, 2, 3, 4]
iterable2 = [1, 2]
result = calculate_difference(iterable1, iterable2)
print(result)

