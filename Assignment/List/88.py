'''Write a  Python program to read a square matrix from the console and print the sum of the matrix's primary diagonal. Accept the size of the square matrix and elements for each column separated with a space (for every row) as input from the user.
Input the size of the matrix: 3
2 3 4
4 5 6
3 4 7
Sum of matrix primary diagonal:
14'''

size = int(input("Input the size of the matrix: "))

# Initialize an empty matrix
matrix = []

# Read the elements of the matrix from the user
print("Input elements row-wise (separated by space):")
for i in range(size):
    row = list(map(int, input().split()))
    matrix.append(row)

# Calculate the sum of the primary diagonal
diagonal_sum = sum(matrix[i][i] for i in range(size))

# Print the sum of the primary diagonal
print("Sum of matrix primary diagonal:")
print(diagonal_sum)
