''' Write a  Python program to move a specified element in a given list.
Original list:
['red', 'green', 'white', 'black', 'orange']
Move white at the end of the said list:
['red', 'green', 'black', 'orange', 'white']
Original list:
['red', 'green', 'white', 'black', 'orange']
Move red at the end of the said list:
['green', 'white', 'black', 'orange', 'red']
Original list:
['red', 'green', 'white', 'black', 'orange']
Move black at the end of the said list:
['red', 'green', 'white', 'orange', 'black']'''


def move_element(lst, element):
    if element in lst:
        lst.remove(element)
        lst.append(element)
        return lst
    else:
        return "Element not found in the list"
original_list = ['red', 'green', 'white', 'black', 'orange']
print("Original list:")
print(original_list)
print("Move white at the end of the said list:")
print(move_element(original_list[:], 'white'))
print("Original list:")
print(original_list)
print("Move red at the end of the said list:")
print(move_element(original_list[:], 'red'))

# Move black at the end of the list
print("Original list:")
print(original_list)
print("Move black at the end of the said list:")
print(move_element(original_list[:], 'black'))
