''' Write a  Python program to check if two lists have the same elements in them in same order or not.
Original lists:
['red', 'green', 'black', 'orange']
['red', 'pink', 'green', 'white', 'black']
['white', 'orange', 'pink', 'black']
Test common elements between color1 and color2 are in same order?
True
Test common elements between color1 and color3 are in same order?
False
Test common elements between color2 and color3 are in same order?
False'''

def check_same_order(list1, list2):
    common_elements = set(list1) & set(list2)
    indices_list1 = [list1.index(element) for element in common_elements]
    indices_list2 = [list2.index(element) for element in common_elements]

    return indices_list1 == indices_list2

color1 = ['red', 'green', 'black', 'orange']
color2 = ['red', 'pink', 'green', 'white', 'black']
color3 = ['white', 'orange', 'pink', 'black']

print("Test common elements between color1 and color2 are in same order?")
print(check_same_order(color1, color2))
print("Test common elements between color1 and color3 are in same order?")
print(check_same_order(color1, color3))
print("Test common elements between color2 and color3 are in same order?")
print(check_same_order(color2, color3))
