'''Write a Python program to rotate a Deque Object a specified number (positive) of times.
Sample Output:
Deque before rotation:
deque([2, 4, 6, 8, 10])
Deque after 1 positive rotation:
deque([10, 2, 4, 6, 8])
Deque after 2 positive rotations:
deque([6, 8, 10, 2, 4])'''

from collections import deque

my_deque = deque([2, 4, 6, 8, 10])
print("Deque before rotation:")
print(my_deque)

for i in range(1, 3):
    my_deque.rotate(-1)  
    print("Deque after {} positive rotation:".format(i))
    print(my_deque)
