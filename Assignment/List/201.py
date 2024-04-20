'''Write a  Python program to check if a given string contains an element that is present in a list.
The original string and list:
https://www.w3resource.com/python-exercises/list/
['.com', '.edu', '.tv']
Check if https://www.w3resource.com/python-exercises/list/ contains an element, which is present in the list ['.com', '.edu', '.tv']
True
The original string and list: https://www.w3resource.net
https://www.w3resource.net
['.com', '.edu', '.tv']
Check if https://www.w3resource.net contains an element, which is present in the list ['.com', '.edu', '.tv']
False'''

def contains_element(string, elements):
    for element in elements:
        if element in string:
            return True
    return False

original_string1 = "https://www.w3resource.com/python-exercises/list/"
original_list1 = [".com", ".edu", ".tv"]
print("The original string and list:")
print(original_string1)
print(original_list1)
print("Check if", original_string1, "contains an element, which is present in the list", original_list1)
print(contains_element(original_string1, original_list1))

original_string2 = "https://www.w3resource.net"
original_list2 = [".com", ".edu", ".tv"]
print("\nThe original string and list:")
print(original_string2)
print(original_list2)
print("Check if", original_string2, "contains an element, which is present in the list", original_list2)
print(contains_element(original_string2, original_list2))
