'''Write a Python program to extract common index elements from more than one given list.
Original lists:
[1, 1, 3, 4, 5, 6, 7]
[0, 1, 2, 3, 4, 5, 7]
[0, 1, 2, 3, 4, 5, 7]
Common index elements of the said lists:
[1, 7]'''

def common_elements(*lists):
    for elements in zip(*lists):
        if all(element == elements[0] for element in elements):
            yield elements[0]

list1 = [1, 1, 3, 4, 5, 6, 7]
list2 = [0, 1, 2, 3, 4, 5, 7]
list3 = [0, 1, 2, 3, 4, 5, 7]

common_elements_list = list(common_elements(list1, list2, list3))

print("Original lists:")
print(list1)
print(list2)
print(list3)
print("Common index elements of the said lists:")
print(common_elements_list)
