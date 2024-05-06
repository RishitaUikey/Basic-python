# Write a Python program to slice a tuple.

x = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
slice1 = x[2:5]
slice2 = x[:3]
slice3 = x[5:]
slice4 = x[::2]
slice5 = x[-3:-1]

print("Elements from index 2 to 5:", slice1)
print("Elements from beginning to index 3:", slice2)
print("Elements from index 5 to the end:", slice3)
print("Every second element:", slice4)
print("Elements from -3 to -1 index:", slice5)