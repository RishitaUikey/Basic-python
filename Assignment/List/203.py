'''Write a  Python program to join adjacent members of a given list.
Original list:
['1', '2', '3', '4', '5', '6', '7', '8']
Join adjacent members of a given list:
['12', '34', '56', '78']
Original list:
['1', '2', '3']
Join adjacent members of a given list:
['12']'''

def join_adjacent_members(lst):
    joined_list = []
    for i in range(0, len(lst), 2):
    
        joined_list.append(''.join(lst[i:i+2]))
    return joined_list

original_list1 = ['1', '2', '3', '4', '5', '6', '7', '8']
print("Original list:")
print(original_list1)
print("Join adjacent members of the given list:")
print(join_adjacent_members(original_list1))

original_list2 = ['1', '2', '3']
print("\nOriginal list:")
print(original_list2)
print("Join adjacent members of the given list:")
print(join_adjacent_members(original_list2))
