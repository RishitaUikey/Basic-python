'''Write a  Python program to filter even numbers from a dictionary of values.
Original Dictionary:
{'V': [1, 4, 6, 10], 'VI': [1, 4, 12], 'VII': [1, 3, 8]}
Filter even numbers from said dictionary values:
{'V': [4, 6, 10], 'VI': [4, 12], 'VII': [8]}
Original Dictionary:
{'V': [1, 3, 5], 'VI': [1, 5], 'VII': [2, 7, 9]}
Filter even numbers from said dictionary values:
{'V': [], 'VI': [], 'VII': [2]}'''

original_dict1 = {'V': [1, 4, 6, 10], 'VI': [1, 4, 12], 'VII': [1, 3, 8]}
original_dict2 = {'V': [1, 3, 5], 'VI': [1, 5], 'VII': [2, 7, 9]}

filtered_dict1 = {key: [num for num in value if num % 2 == 0] for key, value in original_dict1.items()}
filtered_dict2 = {key: [num for num in value if num % 2 == 0] for key, value in original_dict2.items()}

print("Original Dictionary:")
print(original_dict1)
print("Filter even numbers from said dictionary values:")
print(filtered_dict1)

print("\nOriginal Dictionary:")
print(original_dict2)
print("Filter even numbers from said dictionary values:")
print(filtered_dict2)
