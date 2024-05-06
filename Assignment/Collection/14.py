'''Write a  Python program to rotate a deque Object a specified number (negative) of times.
Sample Output:
Deque before rotation:
deque([2, 4, 6, 8, 10])
Deque after 1 negative rotation:
deque([4, 6, 8, 10, 2])
Deque after 2 negative rotations:
deque([8, 10, 2, 4, 6])'''

from collections import deque

my_deque = deque([2, 4, 6, 8, 10])
print("Deque before rotation:")
print(my_deque)

for i in range(1, 3):
    my_deque.rotate(1)  
    print("Deque after {} negative rotation:".format(i))
    print(my_deque)
