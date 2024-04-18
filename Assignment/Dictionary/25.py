#  Write a  Python program to print a dictionary in table format.

from tabulate import tabulate

# Sample dictionary
data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'City': ['New York', 'Los Angeles', 'Chicago']}

# Convert dictionary to list of lists
table = [[key] + value for key, value in data.items()]

# Print table
print(tabulate(table, headers="firstrow", tablefmt="grid"))
