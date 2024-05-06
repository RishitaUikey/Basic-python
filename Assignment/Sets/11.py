# Write a  Python program to create a shallow copy of sets.
#Note : Shallow copy is a bit-wise copy of an object. A new object is created 
# that has an exact copy of the values in the original object.

original_set = {1, 2, 3, 4, 5}
shallow_copy1 = original_set.copy()
shallow_copy2 = set(original_set)

print("Original set:", original_set)
print("Shallow copy 1:", shallow_copy1)
print("Shallow copy 2:", shallow_copy2)

shallow_copy1.add(6)
shallow_copy2.remove(1)

print("Modified shallow copy 1:", shallow_copy1)
print("Modified shallow copy 2:", shallow_copy2)
print("Original set after modifications:", original_set)
