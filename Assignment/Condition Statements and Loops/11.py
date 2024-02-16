'''Write a Python program that takes two digits m (row) and n (column) 
as input and generates a two-dimensional array. The element value in 
the i-th row and j-th column of the array should be i*j.
Note :
i = 0,1.., m-1
j = 0,1, n-1.

Test Data : Rows = 3, Columns = 4
Expected Result : [[0, 0, 0, 0], [0, 1, 2, 3], [0, 2, 4, 6]]'''

# Taking input for rows and columns
rows = int(input("Enter the number of rows: "))
columns = int(input("Enter the number of columns: "))

# Generating the two-dimensional array
two_dimensional_array = []

for i in range(rows):
    row = []
    for j in range(columns):
        row.append(i * j)
    two_dimensional_array.append(row)

# Printing the two-dimensional array
print("Resultant 2D Array:")
for row in two_dimensional_array:
    print(row,end=',')
