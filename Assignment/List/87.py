'''Write a  Python program to read a matrix from the console and print the sum for each column. As input from the user, accept matrix rows, columns, and elements separated by a space (each row).
Input rows: 2
Input columns: 2
Input number of elements in a row (1, 2, 3):
1 2
3 4
sum for each column:
4 6'''

rows = int(input("Input rows: "))
cols = int(input("Input columns: "))

matrix = []

print("Input elements row-wise (separated by space):")
for i in range(rows):
    row = list(map(int, input().split()))
    matrix.append(row)

column_sums = [sum(col) for col in zip(*matrix)]

print("Sum for each column:")
print(*column_sums)
