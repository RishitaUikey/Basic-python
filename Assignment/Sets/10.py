#  Write a  Python program to check if a set is a subset of another set.

s1 = {1, 2, 3}
s2 = {1, 2, 3, 4, 5}
subset = s1.issubset(s2)
if subset:
    print("set1 is a subset of set2")
else:
    print("set1 is not a subset of set2")

