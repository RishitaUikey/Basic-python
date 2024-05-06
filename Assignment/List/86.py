'''Write a Python program to create a 3X3 grid with numbers.
3X3 grid with numbers:
[[1, 2, 3], [1, 2, 3], [1, 2, 3]]'''

rows = 3
cols = 3
grid = [[col + 1 for col in range(cols)] for _ in range(rows)]

print("3x3 grid with numbers:")
for row in grid:
    print(row)
