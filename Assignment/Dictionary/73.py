'''Write a  Python program to convert a list of dictionaries into a list of values corresponding to the specified key.
Sample Output:
Original list of dictionaries:
[{'name': 'Theodore', 'age': 18}, {'name': 'Mathew', 'age': 22}, {'name': 'Roxanne', 'age': 20}, {'name': 'David', 'age': 18}]
Convert a list of dictionaries into a list of values corresponding to the specified key:
[18, 22, 20, 18]'''

def extract_values(data, key):
    return [item[key] for item in data]

original_list = [
    {'name': 'Theodore', 'age': 18},
    {'name': 'Mathew', 'age': 22},
    {'name': 'Roxanne', 'age': 20},
    {'name': 'David', 'age': 18}
]

specified_key = 'age'
result = extract_values(original_list, specified_key)

print("Original list of dictionaries:")
print(original_list)
print("Convert a list of dictionaries into a list of values corresponding to the specified key:")
print(result)
