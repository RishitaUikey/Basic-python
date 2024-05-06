'''Write a  Python program that takes any number of iterable objects or objects with a length property and returns the longest one.
Sample Output:
Green
[1, 2, 3, 4, 5]
[1, 2, 3, 4]'''

def longest_iterable(*args):
    return max(args, key=len)
sample1 = "Red"
sample2 = [1, 2, 3, 4, 5]
sample3 = [1, 2, 3, 4]
longest = longest_iterable(sample1, sample2, sample3)
print(longest)
