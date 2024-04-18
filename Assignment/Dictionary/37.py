# Write a  Python program to replace dictionary values with their sums.

sample_dict = {'a': [1, 2, 3], 'b': [4, 5], 'c': [6, 7, 8]}
for key in sample_dict:
    sample_dict[key] = sum(sample_dict[key])
print(sample_dict)
