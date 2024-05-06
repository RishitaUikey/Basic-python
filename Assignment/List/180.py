'''Write a  Python program to create the smallest possible number using the elements of a given list of positive integers.
Original list:
[3, 40, 41, 43, 74, 9]
Smallest possible number using the elements of the said list of positive integers:
3404143749
Original list:
[10, 40, 20, 30, 50, 60]
Smallest possible number using the elements of the said list of positive integers:
102030405060
Original list:
[8, 4, 2, 9, 5, 6, 1, 0]
Smallest possible number using the elements of the said list of positive integers:
01245689'''

from typing import List

def smallest_possible_number(nums: List[int]) -> str:
    def compare(a: int, b: int) -> int:
        return int(str(a) + str(b)) - int(str(b) + str(a))
    nums.sort(key=lambda x: (len(str(x)), x), reverse=False)
    return ''.join(map(str, nums))

original_lists = [
    [3, 40, 41, 43, 74, 9],
    [10, 40, 20, 30, 50, 60],
    [8, 4, 2, 9, 5, 6, 1, 0]
]

for nums in original_lists:
    print("Original list:")
    print(nums)
    print("Smallest possible number using the elements of the said list of positive integers:")
    print(smallest_possible_number(nums))
    print()
