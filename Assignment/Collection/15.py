'''Write a  Python program to find the most common element in a given list.
Sample Output:
Original list:
['PHP', 'PHP', 'Python', 'PHP', 'Python', 'JS', 'Python', 'Python', 'PHP', 'Python']
Most common element of the said list:
Python'''

from collections import Counter

x = ['PHP', 'PHP', 'Python', 'PHP', 'Python', 'JS', 'Python', 'Python', 'PHP', 'Python']
most_common_element = Counter(x).most_common(1)[0][0]

print("Most common element of the said list:")
print(most_common_element)
