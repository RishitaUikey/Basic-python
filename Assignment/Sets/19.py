# Write a Python program to find elements in a given set that are not in another set.

s1 = {1, 2, 3, 4, 5}
s2 = {4, 5, 6, 7, 8}

differenceset = s1.difference(s2)

# Display the elements in set1 that are not in set2
print("Elements in set1 that are not in set2:", differenceset)
