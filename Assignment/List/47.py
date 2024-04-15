# Write a Python program to insert an element before each element of a list.

color = ['Red','Yellow','Orange','Blue', 'Green', 'Black']
print("Original List: ", color)

color = [v for elt in color for v in ('colour', elt)]
print("Updated List: ", color)