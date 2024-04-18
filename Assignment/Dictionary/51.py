'''A  Python Dictionary contains List as a value. Write a Python program to update the list values in the said dictionary.
Original Dictionary:
{'Math': [88, 89, 90], 'Physics': [92, 94, 89], 'Chemistry': [90, 87, 93]}
Update the list values of the said dictionary:
{'Math': [89, 90, 91], 'Physics': [90, 92, 87], 'Chemistry': [90, 87, 93]}'''

original_dict = {'Math': [88, 89, 90], 'Physics': [92, 94, 89], 'Chemistry': [90, 87, 93]}

for key, value in original_dict.items():
    updated_list = [item + 1 for item in value] 
    original_dict[key] = updated_list

print("Update the list values of the said dictionary:")
print(original_dict)
