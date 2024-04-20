'''Write a  Python program to create a new list by dividing two given lists of numbers.
Original list:
[7, 2, 3, 4, 9, 2, 3]
[7, 2, 3, 4, 9, 2, 3]
[0.7777777777777778, 0.25, 1.5, 1.3333333333333333, 3.0, 2.0, 1.5]'''

def divide_lists(list1, list2):
    result = []
    for num1, num2 in zip(list1, list2):
        if num2 != 0:
    
            result.append(num1 / num2)
        else:
            result.append(None)
    
    return result

list1 = [7, 2, 3, 4, 9, 2, 3]
list2 = [7, 2, 3, 4, 9, 2, 3]
list3 = [0.7777777777777778, 0.25, 1.5, 1.3333333333333333, 3.0, 2.0, 1.5]

print("Original list 1:")
print(list1)
print("Original list 2:")
print(list2)
print("Result of dividing list 1 by list 2:")
print(divide_lists(list1, list2))
print("Original list 3:")
print(list3)
