'''Write a  Python program to add more elements to a deque object from an iterable object.
Sample Output:
Even numbers:
deque([2, 4, 6, 8, 10])
More even numbers:
deque([2, 4, 6, 8, 10, 12, 14, 16, 18, 20])'''

from collections import deque

even_numbers = deque([2, 4, 6, 8, 10])
print("Even numbers:")
print(even_numbers)

more_even_numbers = range(12, 21, 2)
even_numbers.extend(more_even_numbers)

print("More even numbers:")
print(even_numbers)
