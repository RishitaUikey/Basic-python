'''Write a  Python program to iterate a given list cyclically at a specific index position.
Original list:
['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
Iterate the said list cyclically on specific index position 3 :
['d', 'e', 'f', 'g', 'h', 'a', 'b', 'c']
Iterate the said list cyclically on specific index position 5 :
['f', 'g', 'h', 'a', 'b', 'c', 'd', 'e']'''

def cyclic_iteration(lst, index):
    first_part = lst[index:]
    second_part = lst[:index]
    result = first_part + second_part
    return result
original_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
index_positions = [3, 5]

for index in index_positions:
    print("Original list:")
    print(original_list)
    print("Iterate the said list cyclically on specific index position", index, ":")
    print(cyclic_iteration(original_list, index))
    print()
