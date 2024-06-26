'''Write a Python program to remove all the elements of a given deque object.
Sample Output:
Original Deque object with odd numbers:
deque([1, 3, 5, 7, 9])
Deque length: 5
Deque object after removing all numbers- deque([])
Deque length:0'''

from collections import deque

odd_numbers = deque([1, 3, 5, 7, 9])
print("Original Deque object with odd numbers:")
print(odd_numbers)

print("Deque length:", len(odd_numbers))
odd_numbers.clear()

print("Deque object after removing all numbers-", odd_numbers)
print("Deque length:", len(odd_numbers))
