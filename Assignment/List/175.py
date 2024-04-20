'''Write a  Python program to find the minimum and maximum value for each tuple position in a given list of tuples.
Original list:
[(2, 3), (2, 4), (0, 6), (7, 1)]
Maximum value for each tuple position in the said list of tuples:
[7, 6]
Minimum value for each tuple position in the said list of tuples:
[0, 1]'''

def min_max_tuples(lst):
    min_values = [float('inf')] * len(lst[0])
    max_values = [float('-inf')] * len(lst[0])
    for tup in lst:
        for i, val in enumerate(tup):
            min_values[i] = min(min_values[i], val)
            max_values[i] = max(max_values[i], val)
    
    return min_values, max_values
original_list = [(2, 3), (2, 4), (0, 6), (7, 1)]
print("Original list:")
print(original_list)
min_values, max_values = min_max_tuples(original_list)
print("\nMaximum value for each tuple position in the said list of tuples:")
print(max_values)
print("Minimum value for each tuple position in the said list of tuples:")
print(min_values)
