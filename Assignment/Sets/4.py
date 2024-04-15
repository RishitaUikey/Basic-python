# Write a Python program to remove item(s) from a given set.

s = {1, 2, 3, 4, 5}
s.remove(3)
s.discard(5)
popped_item = s.pop()
print("Updated set:", s)
print("Popped item:", popped_item)
