'''Write a  Python program that copies a deque object and verifies shallow copying.
Sample Output:
Content of dq1:
deque([1, 3, 5, 7, 9])
dq2 id:
140706429557152
Content of dq2:
deque([1, 3, 5, 7, 9])
dq2 id:
140706406914152
Checking the first element of dq1 and dq2 are shallow copies:
11065888
11065888'''

from collections import deque
import copy

dq1 = deque([1, 3, 5, 7, 9])

print("Content of dq1:")
print(dq1)

dq2 = copy.copy(dq1)

print("dq2 id:")
print(id(dq2))

print("Content of dq2:")
print(dq2)

print("dq2 id:")
print(id(dq2))

print("Checking the first element of dq1 and dq2 are shallow copies:")
print(id(dq1[0]))
print(id(dq2[0]))
