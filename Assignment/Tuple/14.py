# Write a Python program to find the index of an item in a tuple.

x = ('apple', 'banana', 'cherry', 'date', 'elderberry')
find = 'cherry'

try:
    index = x.index(find)
    print(f"The index of '{find}' is: {index}")
except ValueError:
    print(f"'{find}' is not in the tuple.")

item_to_find = 'fig'

try:
    index = x.index(item_to_find)
    print(f"The index of '{item_to_find}' is: {index}")
except ValueError:
    print(f"'{item_to_find}' is not in the tuple.")
