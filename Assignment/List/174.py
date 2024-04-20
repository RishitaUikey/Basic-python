'''Write a  Python program to add a number to each element in a given list of numbers.
Original lists:
[3, 8, 9, 4, 5, 0, 5, 0, 3]
Add 3 to each element in the said list:
[6, 11, 12, 7, 8, 3, 8, 3, 6]
Original lists:
[3.2, 8, 9.9, 4.2, 5, 0.1, 5, 3.11, 0]
Add 0.51 to each element in the said list:
[3.71, 8.51, 10.41, 4.71, 5.51, 0.61, 5.51, 3.62, 0.51]'''

def add_number_to_list(lst, num):
    return [x + num for x in lst]

original_list1 = [3, 8, 9, 4, 5, 0, 5, 0, 3]
number1 = 3
result1 = add_number_to_list(original_list1, number1)
print("Original list:", original_list1)
print("Add", number1, "to each element in the said list:")
print(result1)
original_list2 = [3.2, 8, 9.9, 4.2, 5, 0.1, 5, 3.11, 0]
number2 = 0.51
result2 = add_number_to_list(original_list2, number2)
print("\nOriginal list:", original_list2)
print("Add", number2, "to each element in the said list:")
print(result2)
