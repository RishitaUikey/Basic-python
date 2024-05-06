'''Write a  Python program to create a multidimensional list (lists of lists) with zeros.
Multidimensional list: [[0, 0], [0, 0], [0, 0]]'''

rows = 3
cols = 2
multidimensional_list = [[0] * cols for _ in range(rows)]
print("Multidimensional list:", multidimensional_list)
