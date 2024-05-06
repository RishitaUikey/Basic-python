'''Write a  Python program to remove a specified dictionary from a given list.
Original list of dictionary:
[{'id': '#FF0000', 'color': 'Red'}, {'id': '#800000', 'color': 'Maroon'}, {'id': '#FFFF00', 'color': 'Yellow'}, {'id': '#808000', 'color': 'Olive'}]
Remove id #FF0000 from the said list of dictionary:
[{'id': '#800000', 'color': 'Maroon'}, {'id': '#FFFF00', 'color': 'Yellow'}, {'id': '#808000', 'color': 'Olive'}]'''

original_list = [
    {'id': '#FF0000', 'color': 'Red'},
    {'id': '#800000', 'color': 'Maroon'},
    {'id': '#FFFF00', 'color': 'Yellow'},
    {'id': '#808000', 'color': 'Olive'}
]

to_remove = {'id': '#FF0000', 'color': 'Red'}
new_list = [d for d in original_list if d != to_remove]
print("Remove id #FF0000 from the list of dictionaries:")
print(new_list)
