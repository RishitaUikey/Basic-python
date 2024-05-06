# Write a Python program to remove the intersection of a second set with a first set.

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

set1.update(set2)

# Display the modified set1
print("Set1 after removing the intersection with set2:", set1)
