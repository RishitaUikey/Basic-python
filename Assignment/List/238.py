
''' Write a Python program to calculate the average of a given list, after mapping each element to a value using the provided function.
Sample Output:
5.0
15.0'''

def map_and_average(lst, func):
    mapped_values = [func(x) for x in lst]
    average = sum(mapped_values) / len(mapped_values)
    return average

def double(x):
    return x * 2

list1 = [1, 2, 3, 4, 5]
list2 = [5, 10, 15, 20, 25]
average1 = map_and_average(list1, double)
print(average1)
average2 = map_and_average(list2, double)
print(average2)

