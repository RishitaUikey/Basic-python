'''Write a  Python program to remove an element from a given list.
Original list:
['Ricky Rivera', 98, 'Math', 90, 'Science']
After deleting an element:, using index of the element: [98, 'Math', 90, 'Science']'''

def remove_element_by_index(lst, index):

    if index < len(lst):
        lst.pop(index) 
    else:
        print("Index out of range")
    return lst

original_list = ['Ricky Rivera', 98, 'Math', 90, 'Science']
index_to_remove = 0  

print("Original list:")
print(original_list)
new_list = remove_element_by_index(original_list, index_to_remove)
print("After deleting an element, using index of the element:")
print(new_list)
