'''Write a  Python program to create a deque and append a few elements to the left and right. Next, remove some elements from the left and right sides and reverse the deque.
Sample Output:
deque(['Red', 'Green', 'White'])
Adding to the left:
deque(['Pink', 'Red', 'Green', 'White'])
Adding to the right:
deque(['Pink', 'Red', 'Green', 'White', 'Orange'])
Removing from the right:
deque(['Pink', 'Red', 'Green', 'White'])
Removing from the left:
deque(['Red', 'Green', 'White'])
Reversing the deque:
deque(['White', 'Green', 'Red'])'''

from collections import deque

my_deque = deque(['Red', 'Green', 'White'])
print("deque({})".format(list(my_deque)))
my_deque.appendleft('Pink')
print("Adding to the left:")
print("deque({})".format(list(my_deque)))

my_deque.append('Orange')
print("Adding to the right:")
print("deque({})".format(list(my_deque)))

my_deque.pop()
print("Removing from the right:")
print("deque({})".format(list(my_deque)))

my_deque.popleft()
print("Removing from the left:")
print("deque({})".format(list(my_deque)))

my_deque.reverse()
print("Reversing the deque:")
print("deque({})".format(list(my_deque)))
