# Write a Python program to remove key-value pairs from a list of dictionaries.

data = [
    {'name': 'Alice', 'age': 25},{'name': 'Bob', 'age': 30},{'name': 'Charlie', 'age': 25},{'name': 'David', 'age': 30}
]
remove = 'age'
exclude = 30
filtered_data = [d for d in data if d.get(remove) != exclude]
print("Filtered list:", filtered_data)
