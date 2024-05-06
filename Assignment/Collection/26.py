'''Write a  Python program to find the difference between two lists including duplicate elements. Use the collections module.
Sample Output:
Original lists:
[3, 3, 4, 7]'''

from collections import Counter


l1 = [3, 3, 4, 7]
l2 = [3, 4, 5, 6]
count1 = Counter(l1)
count2 = Counter(l2)
difference = count1 - count2

print("Difference between the two lists:")
print(list(difference.elements()))
