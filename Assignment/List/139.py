'''Write a  Python program to sort a given list of strings(numbers) numerically.
Original list:
['4', '12', '45', '7', '0', '100', '200', '-12', '-500']
Sort the said list of strings(numbers) numerically:
[-500, -12, 0, 4, 7, 12, 45, 100, 200]'''


def sort_numerically(lst):
    sorted_list = sorted(map(int, lst))
    sorted_strings = [str(num) for num in sorted_list]
    return sorted_strings


original_list = ['4', '12', '45', '7', '0', '100', '200', '-12', '-500']
sorted_list = sort_numerically(original_list)
print("Sort the said list of strings(numbers) numerically:")
print(sorted_list)
