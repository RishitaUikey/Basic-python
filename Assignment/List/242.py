'''Write a Python program to get the symmetric difference between two iterables, without filtering out duplicate values.
Sample Output:
[30, 40]'''

def symmetric_difference(iterable1, iterable2):
    set1 = set(iterable1)
    set2 = set(iterable2)
    return list(set1.symmetric_difference(set2))
iterable1 = [10, 20, 30, 40]
iterable2 = [20, 30, 50, 60]
result = symmetric_difference(iterable1, iterable2)
print(result)
