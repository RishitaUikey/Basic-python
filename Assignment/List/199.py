'''Write a  Python program to convert a Unicode list to a list of strings.
Original lists:
['S001', 'S002', 'S003', 'S004']
Convert the said unicode list to a list contains strings:
['S001', 'S002', 'S003', 'S004']
Click me to see the sample solution

200. Write a  Python program to pair consecutive elements of a given list.
Original lists:
[1, 2, 3, 4, 5, 6]
Pair up the consecutive elements of the said list:
[[1, 2], [2, 3], [3, 4], [4, 5], [5, 6]]
Original lists:
[1, 2, 3, 4, 5]
Pair up the consecutive elements of the said list:
[[1, 2], [2, 3], [3, 4], [4, 5]]'''

def unicode_to_strings(unicode_list):
    return [str(item) for item in unicode_list]

def pair_consecutive_elements(input_list):
    return [[input_list[i], input_list[i+1]] for i in range(len(input_list) - 1)]

unicode_list = ['S001', 'S002', 'S003', 'S004']
input_lists = [
    [1, 2, 3, 4, 5, 6],
    [1, 2, 3, 4, 5]
]

print("Original lists:")
print(unicode_list)
print("Convert the said unicode list to a list contains strings:")
print(unicode_to_strings(unicode_list))
for lst in input_lists:
    print("\nOriginal list:")
    print(lst)
    print("Pair up the consecutive elements of the said list:")
    print(pair_consecutive_elements(lst))
