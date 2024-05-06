'''Write a  Python program to generate a list of numbers in the arithmetic progression starting with the given positive integer and up to the specified limit.
Sample Output:
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
[3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36]
[5, 10, 15, 20, 25]'''

def arithmetic_progression(start, limit, step):
    return list(range(start, limit + 1, step))
sample_inputs = [
    (1, 15, 1),
    (3, 36, 3),
    (5, 25, 5)
]
for start, limit, step in sample_inputs:
    print(arithmetic_progression(start, limit, step))
