''' Write a  Python program that iterates over elements as many times as its count.
Sample Output: ['p', 'p', 'p', 'p', 'q', 'q']'''

elements = ['p', 'q']
counts = {'p': 4, 'q': 2}
output = [i for i in elements for _ in range(counts[i])]
print(output)
