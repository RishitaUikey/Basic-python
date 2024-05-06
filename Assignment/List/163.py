'''Write a  Python program to get the index of the first element that is greater than a specified element.
Original list:
[12, 45, 23, 67, 78, 90, 100, 76, 38, 62, 73, 29, 83]
Index of the first element which is greater than 73 in the said list:
4
Index of the first element which is greater than 21 in the said list:
1
Index of the first element which is greater than 80 in the said list:
5
Index of the first element which is greater than 55 in the said list:
3'''

def first_greater_index(lst, value):
    for i, num in enumerate(lst):
        if num > value:
            return i
    return -1 

original_list = [12, 45, 23, 67, 78, 90, 100, 76, 38, 62, 73, 29, 83]
values_to_check = [73, 21, 80, 55]
for value in values_to_check:
    print(f"Index of the first element which is greater than {value} in the said list:")
    print(first_greater_index(original_list, value))
