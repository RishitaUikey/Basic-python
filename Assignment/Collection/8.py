'''Write a  Python program to create a deque from an existing iterable object.
Sample Output:
Original tuple:
(2, 4, 6)
<class 'tuple'>
Original deque:
deque([2, 4, 6])
New deque from an existing iterable object:
deque([2, 2, 4, 6, 8, 10, 12])
<class 'collections.deque'>'''

from collections import deque

original_tuple = (2, 4, 6)
print("Original tuple:")
print(original_tuple)
print(type(original_tuple))

original_deque = deque(original_tuple)
print("Original deque:")
print(original_deque)

new_iterable = [8, 10, 12]

original_deque.extend(new_iterable)
print("New deque from an existing iterable object:")
print(original_deque)
print(type(original_deque))
