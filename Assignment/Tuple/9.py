# Write a  Python program to find repeated items in a tuple.

x = (1, 2, 3, 4, 2, 6, 3, 9, 1, 2)
repeated = []
for i in x:
    if x.count(i) > 1 and i not in repeated:
        repeated.append(i)
print("Repeated items in the tuple:",repeated)