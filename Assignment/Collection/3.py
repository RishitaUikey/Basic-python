'''Write a Python program to create a new deque with three items and iterate over the deque's elements.
Sample Output:
a
e
i
o
u'''

from collections import deque

x = deque(['a', 'e', 'i'])
x.append('o')
x.appendleft('u')

for item in x:
    print(item)
