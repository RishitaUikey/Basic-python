''' Write a  Python program to join two given list of lists of the same length, element wise.
Original lists:
[[10, 20], [30, 40], [50, 60], [30, 20, 80]]
[[61], [12, 14, 15], [12, 13, 19, 20], [12]]
Join the said two lists element wise:
[[10, 20, 61], [30, 40, 12, 14, 15], [50, 60, 12, 13, 19, 20], [30, 20, 80, 12]]
Original lists:
[['a', 'b'], ['b', 'c', 'd'], ['e', 'f']]
[['p', 'q'], ['p', 's', 't'], ['u', 'v', 'w']]
Join the said two lists element wise:
[['a', 'b', 'p', 'q'], ['b', 'c', 'd', 'p', 's', 't'], ['e', 'f', 'u', 'v', 'w']]'''

def join_lists(list1, list2):
    return [sublist1 + sublist2 for sublist1, sublist2 in zip(list1, list2)]

original_list1 = [[10, 20], [30, 40], [50, 60], [30, 20, 80]]
original_list2 = [[61], [12, 14, 15], [12, 13, 19, 20], [12]]
print("Join the said two lists element wise:")
print(join_lists(original_list1, original_list2))
original_list3 = [['a', 'b'], ['b', 'c', 'd'], ['e', 'f']]
original_list4 = [['p', 'q'], ['p', 's', 't'], ['u', 'v', 'w']]
print("Join the said two lists element wise:")
print(join_lists(original_list3, original_list4))
