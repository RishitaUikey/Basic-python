# Write a Python program to check if all items in a given list of strings are equal to a given string.

c1 = ["red", "yellow", "green", "blue"]
c2 = ["blue", "blue", "blue"]
print(all(c == 'green' for c in c1))
print(all(c == 'blue' for c in c2)) 
