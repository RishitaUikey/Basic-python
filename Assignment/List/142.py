'''Write a  Python program to sum a specific column of a list in a given list of lists.
Original list of lists:
[[1, 2, 3, 2], [4, 5, 6, 2], [7, 8, 9, 5]]
Sum: 1st column of the said list of lists:
12
Sum: 2nd column of the said list of lists:
15
Sum: 4th column of the said list of lists:
9'''

def sum_column(list_of_lists, column):
    column_sum = sum(row[column] for row in list_of_lists)
    return column_sum

original_list = [[1, 2, 3, 2], [4, 5, 6, 2], [7, 8, 9, 5]]
sum_1st_column = sum_column(original_list, 0)
sum_2nd_column = sum_column(original_list, 1)
sum_4th_column = sum_column(original_list, 3)
print("Sum: 1st column of the said list of lists:", sum_1st_column)
print("Sum: 2nd column of the said list of lists:", sum_2nd_column)
print("Sum: 4th column of the said list of lists:", sum_4th_column)
