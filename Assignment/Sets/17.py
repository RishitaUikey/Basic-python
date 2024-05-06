# Write a Python program to check if two given sets have no elements in common.

s1 = {1, 2, 3}
s2 = {4, 5, 6}

if s1.isdisjoint(s2):
    print("The sets have no elements in common.")
else:
    print("The sets have elements in common.")
