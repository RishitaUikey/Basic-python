''' Write a  Python program to convert string values of a given dictionary into integer/float datatypes.
Original list:
[{'x': '10', 'y': '20', 'z': '30'}, {'p': '40', 'q': '50', 'r': '60'}]
String values of a given dictionary, into integer types:
[{'x': 10, 'y': 20, 'z': 30}, {'p': 40, 'q': 50, 'r': 60}]
Original list:
[{'x': '10.12', 'y': '20.23', 'z': '30'}, {'p': '40.00', 'q': '50.19', 'r': '60.99'}]
String values of a given dictionary, into float types:
[{'x': 10.12, 'y': 20.23, 'z': 30.0}, {'p': 40.0, 'q': 50.19, 'r': 60.99}]'''

original_list_int = [{'x': '10', 'y': '20', 'z': '30'}, {'p': '40', 'q': '50', 'r': '60'}]
result_int = [{k: int(v) for k, v in d.items()} for d in original_list_int]

print("String values of a given dictionary, into integer types:")
print(result_int)

original_list_float = [{'x': '10.12', 'y': '20.23', 'z': '30'}, {'p': '40.00', 'q': '50.19', 'r': '60.99'}]
result_float = [{k: float(v) for k, v in d.items()} for d in original_list_float]
print("String values of a given dictionary, into float types:")
print(result_float)


