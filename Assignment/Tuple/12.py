# Write a Python program to remove an item from a tuple.

x = (1, 2, 3, 4, 5)
remove = 3
list_temp = list(x)
if remove in list_temp:
    list_temp.remove(remove)
else:
    print(f"Item {remove} not found in the tuple.")
    
new_tuple = tuple(list_temp)

print("New tuple after removing", remove, ":", new_tuple)
