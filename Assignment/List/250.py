'''Write a  Python program to calculate the sum of a list, after mapping each element to a value using the provided function.
Sample Output:
20'''

def map_and_get_sum(lst, func):
    mapped_values = [func(x) for x in lst]
    return sum(mapped_values)

def square(x):
    return x ** 2

sample_list = [1, 2, 3, 4]
sum_value = map_and_get_sum(sample_list, square)
print(sum_value)

