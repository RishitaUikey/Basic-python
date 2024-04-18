# Write a  Python program to check whether an element exists within a tuple.

x = (1, 2, 3, 4, 5,6)
check = 3
if check in x:
    print("Element",check, "exists in the tuple.")
else:
    print("Element", check, "does not exist in the tuple.")