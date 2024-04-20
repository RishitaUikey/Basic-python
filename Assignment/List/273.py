'''Write a  Python program to find an element that divides a given list of integers with the same sum value.
Sample Output:
Original list:
[0, 9, 2, 4, 5, 6]
Element that devides the said list of integers with the same sum value:
4
Original list:
[-4, 0, 6, 1, 0, 2]
Element that devides the said list of integers with the same sum value:
1
Original list:
[1, 2, 3, 4]
Element that devides the said list of integers with the same sum value:
No such element!
Original list:
[-4, 0, 5, 1, 0, 1]
Element that devides the said list of integers with the same sum value:
1'''

def find_element_with_same_sum(lst):
    total_sum = sum(lst)
    left_sum = 0
    for i in range(len(lst)):
        if left_sum == total_sum - left_sum - lst[i]:
            return lst[i]
        left_sum += lst[i]
    return "No such element!"

sample_lists = [
    [0, 9, 2, 4, 5, 6],
    [-4, 0, 6, 1, 0, 2],
    [1, 2, 3, 4],
    [-4, 0, 5, 1, 0, 1]
]

for lst in sample_lists:
    print("Original list:")
    print(lst)
    print("Element that divides the said list of integers with the same sum value:")
    print(find_element_with_same_sum(lst))
