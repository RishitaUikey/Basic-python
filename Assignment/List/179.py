'''Write a  Python program to create the largest possible number using the elements of a given list of positive integers.
Original list:
[3, 40, 41, 43, 74, 9]
Largest possible number using the elements of the said list of positive integers:
9744341403
Original list:
[10, 40, 20, 30, 50, 60]
Largest possible number using the elements of the said list of positive integers:
605040302010
Original list:
[8, 4, 2, 9, 5, 6, 1, 0]
Largest possible number using the elements of the said list of positive integers:
98654210'''

from typing import List

def largest_possible_number(nums: List[int]) -> str:
    def compare(a: int, b: int) -> int:
        return int(str(b) + str(a)) - int(str(a) + str(b))
    nums.sort(key=lambda x: (len(str(x)), x), reverse=True, cmp=compare)
    return ''.join(map(str, nums))
test_cases = [
    [3, 40, 41, 43, 74, 9],
    [10, 40, 20, 30, 50, 60],
    [8, 4, 2, 9, 5, 6, 1, 0]
]
for i, nums in enumerate(test_cases, start=1):
    print(f"Original list {i}:")
    print(nums)
    print(f"Largest possible number using the elements of the said list of positive integers:")
    print(largest_possible_number(nums))
    print()
