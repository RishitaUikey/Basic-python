'''Write a  Python program to check if two given lists contain the same elements regardless of order.
Sample Output:
Original list elements:
[1, 2, 4]
[2, 4, 1]
Check two said lists contain the same elements regardless of order!
True
Original list elements:
[1, 2, 3]
[1, 2, 3]
Check two said lists contain the same elements regardless of order!
True
Original list elements:
[1, 2, 3]
[1, 2, 4]
Check two said lists contain the same elements regardless of order!
False'''

def same_elements_regardless_of_order(list1, list2):
    return set(list1) == set(list2)

sample_lists = [
    ([1, 2, 4], [2, 4, 1]),
    ([1, 2, 3], [1, 2, 3]),
    ([1, 2, 3], [1, 2, 4])
]

for list1, list2 in sample_lists:
    print("Original list elements:")
    print(list1)
    print(list2)
    print("Check two said lists contain the same elements regardless of order!")
    print(same_elements_regardless_of_order(list1, list2))
