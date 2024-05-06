'''Write a  Python program to rotate a given list by a specified number of items in the right or left direction.
original List:
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Rotate the said list in left direction by 4:
[4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4]
Rotate the said list in left direction by 2:
[3, 4, 5, 6, 7, 8, 9, 10, 1, 2]
Rotate the said list in Right direction by 4:
[8, 9, 10, 1, 2, 3, 4, 5, 6]
Rotate the said list in Right direction by 2:
[9, 10, 1, 2, 3, 4, 5, 6, 7, 8]'''

def rotate_list(lst, n, direction='right'):
    if direction == 'left':
        return lst[n % len(lst):] + lst[:n % len(lst)]
    elif direction == 'right':
        return lst[-n % len(lst):] + lst[:-n % len(lst)]
    else:
        return "Invalid direction"

original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
rotated_left_4 = rotate_list(original_list, 4, 'left')
print("Rotate the said list in left direction by 4:")
print(rotated_left_4)
rotated_left_2 = rotate_list(original_list, 2, 'left')
print("Rotate the said list in left direction by 2:")
print(rotated_left_2)
rotated_right_4 = rotate_list(original_list, 4, 'right')
print("Rotate the said list in Right direction by 4:")
print(rotated_right_4)
rotated_right_2 = rotate_list(original_list, 2, 'right')
print("Rotate the said list in Right direction by 2:")
print(rotated_right_2)
