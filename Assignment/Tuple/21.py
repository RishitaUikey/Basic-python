'''Write a Python program to replace the last value of tuples in a list.
Sample list: [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
Expected Output: [(10, 20, 100), (40, 50, 100), (70, 80, 100)]'''

t = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
new = 100
modified_list = [tuple(t[:-1]) + (new,) for t in t]
print("Modified List:", modified_list)