'''Write a  Python program to break a given list of integers into sets of a given positive number. Return true or false.
Sample Output:
Original list: [1, 2, 3, 4, 5, 6, 7, 8]
Number to devide the said list: 4
True
Original list: [1, 2, 3, 4, 5, 6, 7, 8]
Number to devide the said list: 3
False'''

def divide_list_into_sets(lst, num):
    return len(lst) % num == 0

list1 = [1, 2, 3, 4, 5, 6, 7, 8]
num1 = 4
list2 = [1, 2, 3, 4, 5, 6, 7, 8]
num2 = 3

result1 = divide_list_into_sets(list1, num1)
result2 = divide_list_into_sets(list2, num2)

print(result1)
print(result2)
