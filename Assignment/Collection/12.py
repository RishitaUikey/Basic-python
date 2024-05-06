'''Write a  Python program to count the number of times a specific element appears in a deque object.
Sample Output:
Number of 2 in the sequence
5
Number of 4 in the sequence
4'''

from collections import deque

my_deque = deque([2, 2, 2, 2, 2, 4, 4, 4, 4])
count_2 = my_deque.count(2)
print("Number of 2 in the sequence:")
print(count_2)

count_4 = my_deque.count(4)
print("Number of 4 in the sequence:")
print(count_4)
