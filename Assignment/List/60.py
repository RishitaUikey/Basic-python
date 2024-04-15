#  Write a Python program to find a tuple, the smallest second index value from a list of tuples.

a = [(2,3),(4,5),(6,8),(7,8)]
print(min(a, key=lambda n: (n[1], -n[0])))