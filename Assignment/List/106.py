'''Write a  Python program to count integers in a given mixed list.
Original list:
[1, 'abcd', 3, 1.2, 4, 'xyz', 5, 'pqr', 7, -5, -12.22]
Number of integers in the said mixed list:
6'''

def count_integers(mixed_list):
    count = 0
    for item in mixed_list:
        if isinstance(item, int):
            count += 1
    return count

original_list = [1, 'abcd', 3, 1.2, 4, 'xyz', 5, 'pqr', 7, -5, -12.22]
integer_count = count_integers(original_list)
print("Original list:")
print(original_list)
print("Number of integers in the said mixed list:")
print(integer_count)
