'''Write a  Python program to interleave multiple lists of the same length.
Original list:
list1: [1, 2, 3, 4, 5, 6, 7]
list2: [10, 20, 30, 40, 50, 60, 70]
list3: [100, 200, 300, 400, 500, 600, 700]
Interleave multiple lists:
[1, 10, 100, 2, 20, 200, 3, 30, 300, 4, 40, 400, 5, 50, 500, 6, 60, 600, 7, 70, 700]'''

def interleave_lists(*lists):
    interleaved_list = []
    for elements in zip(*lists):
        interleaved_list.extend(elements)
    return interleaved_list

list1 = [1, 2, 3, 4, 5, 6, 7]
list2 = [10, 20, 30, 40, 50, 60, 70]
list3 = [100, 200, 300, 400, 500, 600, 700]

result = interleave_lists(list1, list2, list3)

print("Original list:")
print("list1:", list1)
print("list2:", list2)
print("list3:", list3)
print("Interleave multiple lists:")
print(result)
