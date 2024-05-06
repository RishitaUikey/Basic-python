'''Write a  Python program to find the key of the maximum value in a dictionary.
Sample Output:
Original dictionary elements:
{'Theodore': 19, 'Roxanne': 22, 'Mathew': 21, 'Betty': 20}
Finds the key of the maximum and minimum value of the said dictionary:
('Roxanne', 'Theodore')'''

def key_of_max_value(input_dict):
    max_key = max(input_dict, key=input_dict.get)
    min_key = min(input_dict, key=input_dict.get)
    return max_key, min_key

original_dict = {'Theodore': 19, 'Roxanne': 22, 'Mathew': 21, 'Betty': 20}
max_key, min_key = key_of_max_value(original_dict)

print("Original dictionary elements:")
print(original_dict)
print("Finds the key of the maximum and minimum value of the said dictionary:")
print((max_key, min_key))
