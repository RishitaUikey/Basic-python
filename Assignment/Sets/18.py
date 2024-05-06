# Write a Python program to check if a given set is a superset of itself and a superset of another given set.

set = {1, 2, 3, 4, 5}
if set.issuperset(set):
    print("The set is a superset of itself.")
else:
    print("The set is not a superset of itself.")

anotherset = {3, 4}

if set.issuperset(anotherset):
    print("The set is a superset of the other set.")
else:
    print("The set is not a superset of the other set.")
