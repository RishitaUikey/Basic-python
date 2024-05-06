'''Write a  Python program to find the dimension of a given matrix.
Original list:
[[1, 2], [2, 4]]
Dimension of the said matrix:
(2, 2)
Original list:
[[0, 1, 2], [2, 4, 5]]
Dimension of the said matrix:
(2, 3)
Original list:
[[0, 1, 2], [2, 4, 5], [2, 3, 4]]
Dimension of the said matrix:
(3, 3)'''

def matrix_dimension(matrix):
    rows = len(matrix)
    columns = len(matrix[0]) if matrix else 0
    return rows, columns

original_lists = [
    [[1, 2], [2, 4]],
    [[0, 1, 2], [2, 4, 5]],
    [[0, 1, 2], [2, 4, 5], [2, 3, 4]]
]
for matrix in original_lists:
    dimensions = matrix_dimension(matrix)
    print("Original list:")
    print(matrix)
    print("Dimension of the said matrix:")
    print(dimensions)
    print()
