'''Write a  Python program to remove an empty tuple(s) from a list of tuples.
Sample data: [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
Expected output: [('',), ('a', 'b'), ('a', 'b', 'c'), 'd']'''

data = [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
filtered = [tup for tup in data if tup]
print("Filtered output:", filtered)
