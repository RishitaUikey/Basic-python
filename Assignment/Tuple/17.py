# Write a  Python program to unzip a list of tuples into individual lists.

list_of_tuples = [(1, 'apple', 'red'), (2, 'banana', 'yellow'), (3, 'cherry', 'red')]
numbers, fruits, colors = zip(*list_of_tuples)
numbers_list = list(numbers)
fruits_list = list(fruits)
colors_list = list(colors)
print("Numbers:", numbers_list)
print("Fruits:", fruits_list)
print("Colors:", colors_list)
