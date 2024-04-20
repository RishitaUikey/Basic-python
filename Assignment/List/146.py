'''Write a  Python program to compute the sum of digits of each number in a given list.
Original tuple:
[10, 2, 56]
Sum of digits of each number of the said list of integers:
14
Original tuple:
[10, 20, 4, 5, 'b', 70, 'a']
Sum of digits of each number of the said list of integers:
19
Original tuple:
[10, 20, -4, 5, -70]
Sum of digits of each number of the said list of integers:
19'''

def sum_of_digits(num):
    if isinstance(num, int):
        return sum(int(digit) for digit in str(abs(num)))
    else:
        return 0

def sum_of_digits_in_list(lst):
    return sum(sum_of_digits(num) for num in lst)

lists = [[10, 2, 56], [10, 20, 4, 5, 'b', 70, 'a'], [10, 20, -4, 5, -70]]
for lst in lists:
    print("Original list:")
    print(lst)
    print("Sum of digits of each number of the said list of integers:")
    print(sum_of_digits_in_list(lst))
