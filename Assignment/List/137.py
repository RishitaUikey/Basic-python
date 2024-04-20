'''Write a Python program to find the first even and odd number in a given list of numbers.
Original list:
[1, 3, 5, 7, 4, 1, 6, 8]
First even and odd number of the said list of numbers:
(4, 1)'''

def find_first_even_odd(lst):
    first_even = None
    first_odd = None
    
    for num in lst:
        if num % 2 == 0 and first_even is None:
            first_even = num
        elif num % 2 != 0 and first_odd is None:
            first_odd = num
        if first_even is not None and first_odd is not None:
            break
    
    return first_even, first_odd

original_list = [1, 3, 5, 7, 4, 1, 6, 8]
result = find_first_even_odd(original_list)
print("First even and odd number of the said list of numbers:")
print(result)
