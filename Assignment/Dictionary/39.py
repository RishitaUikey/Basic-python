'''Write a  Python program to store dictionary data in a JSON file.
Original dictionary:
{'students': [{'firstName': 'Nikki', 'lastName': 'Roysden'}, {'firstName': 'Mervin', 'lastName': 'Friedland'}, {'firstName': 'Aron ', 'lastName': 'Wilkins'}], 'teachers': [{'firstName': 'Amberly', 'lastName': 'Calico'}, {'firstName': 'Regine', 'lastName': 'Agtarap'}]}
<class 'dict'>
Json file to dictionary:
{'students': [{'firstName': 'Nikki', 'lastName': 'Roysden'}, {'firstName': 'Mervin', 'lastName': 'Friedland'}, {'firstName': 'Aron ', 'lastName': 'Wilkins'}], 'teachers': [{'firstName': 'Amberly', 'lastName': 'Calico'}, {'firstName': 'Regine', 'lastName': 'Agtarap'}]}'''

import json

original_dict = {
    'students': [
        {'firstName': 'Nikki', 'lastName': 'Roysden'},
        {'firstName': 'Mervin', 'lastName': 'Friedland'},
        {'firstName': 'Aron ', 'lastName': 'Wilkins'}
    ],
    'teachers': [
        {'firstName': 'Amberly', 'lastName': 'Calico'},
        {'firstName': 'Regine', 'lastName': 'Agtarap'}
    ]
}

with open('data.json', 'w') as json_file:
    json.dump(original_dict, json_file)

with open('data.json', 'r') as json_file:
    json_data = json.load(json_file)
    print("Json file to dictionary:")
    print(json_data)
