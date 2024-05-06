'''Write a  Python program to retrieve the value of the nested key indicated by the given selector list from a dictionary or list.
Sample Output:
Harwood
2'''

def get_value(data, selectors):
    current = data
    for selector in selectors:
        if isinstance(current, dict):
            current = current.get(selector)
        elif isinstance(current, list):
            try:
                index = int(selector)
                current = current[index]
            except ValueError:
                return None
        else:
            return None
    return current

sample_dict = {
    "info": {
        "name": "John",
        "age": 30,
        "address": {
            "city": "New York",
            "zipcode": "10001"
        }
    },
    "children": ["Alice", "Bob"]
}

selector1 = ["info", "name"]
selector2 = ["children", "1"]
value1 = get_value(sample_dict, selector1)
value2 = get_value(sample_dict, selector2)
print(value1)
print(value2)
