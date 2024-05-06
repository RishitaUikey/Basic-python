'''Write a Python program to check if a specified element appears in a tuple of tuples.
Original list:
(('Red', 'White', 'Blue'), ('Green', 'Pink', 'Purple'), ('Orange', 'Yellow', 'Lime'))
Check if White presenet in said tuple of tuples!
True
Check if White presenet in said tuple of tuples!
True
Check if Olive presenet in said tuple of tuples!
False'''

t = (('Red', 'White', 'Blue'), ('Green', 'Pink', 'Purple'), ('Orange', 'Yellow', 'Lime'))
check = 'White'
element_present = any(check in t for t in t)
print(f"Check if {check} present in said tuple of tuples!")
print(element_present)
