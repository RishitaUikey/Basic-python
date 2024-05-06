'''Write a  Python program to sort a given matrix in ascending order according to the sum of its rows.
Original Matrix:
[[1, 2, 3], [2, 4, 5], [1, 1, 1]]
Sort the said matrix in ascending order according to the sum of its rows
[[1, 1, 1], [1, 2, 3], [2, 4, 5]]
Original Matrix:
[[1, 2, 3], [-2, 4, -5], [1, -1, 1]]
Sort the said matrix in ascending order according to the sum of its rows
[[-2, 4, -5], [1, -1, 1], [1, 2, 3]]'''

def sort_matrix_by_row_sum(matrix):
    row_sums = [sum(row) for row in matrix]
    sorted_matrix = [row for _, row in sorted(zip(row_sums, matrix))]   
    return sorted_matrix
sample_matrices = [
    [[1, 2, 3], [2, 4, 5], [1, 1, 1]],
    [[1, 2, 3], [-2, 4, -5], [1, -1, 1]]
]
for matrix in sample_matrices:
    print("Original Matrix:")
    for row in matrix:
        print(row)
    print("Sort the said matrix in ascending order according to the sum of its rows")
    sorted_matrix = sort_matrix_by_row_sum(matrix)
    for row in sorted_matrix:
        print(row)
    print()