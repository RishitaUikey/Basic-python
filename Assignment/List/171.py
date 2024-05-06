'''Write a  Python program to concatenate element-wise three given lists.
Original lists:
['0', '1', '2', '3', '4']
['red', 'green', 'black', 'blue', 'white']
['100', '200', '300', '400', '500']
Concatenate element-wise three said lists:
['0red100', '1green200', '2black300', '3blue400', '4white500']'''

def concatenate_lists(list1, list2, list3):
    return [a + b + c for a, b, c in zip(list1, list2, list3)]

list1 = ['0', '1', '2', '3', '4']
list2 = ['red', 'green', 'black', 'blue', 'white']
list3 = ['100', '200', '300', '400', '500']
result = concatenate_lists(list1, list2, list3)
print("Concatenate element-wise three said lists:")
print(result)
