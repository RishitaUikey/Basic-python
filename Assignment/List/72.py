'''Write a Python program to flatten a given nested list structure.
Original list: [0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]]
Flatten list:
[0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]'''

original_list = [0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]]
flattened = []
for item in original_list:
    if isinstance(item, list):
        for sub_item in item:
            flattened.append(sub_item)
    else:
        flattened.append(item)
print("Original list:", original_list)
print("Flatten list:", flattened)
