'''Write a  Python program to find the majority element from a given array of size n using the Collections module.
Sample Output:
10'''

from collections import Counter

def majority_element(nums):
    counts = Counter(nums)
    majority_element = max(counts, key=counts.get)
    return majority_element

array = [10, 20, 30, 10, 10, 10, 20]
result = majority_element(array)
print(result)
