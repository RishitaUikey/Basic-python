'''Write a Python program to find the highest 3 values of corresponding keys in a dictionary.'''

data = {'a': 100, 'b': 200, 'c': 300, 'd': 400, 'e': 500}
sorted_data = sorted(data.items(), key=lambda x: x[1], reverse=True)
top_3 = sorted_data[:3]
for key, value in top_3:
    print(f"{key}: {value}")
