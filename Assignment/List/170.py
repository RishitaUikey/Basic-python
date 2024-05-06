''' Write a  Python program to insert an element in a given list after every nth position.
Original list:
[1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
Insert a in the said list after 2 nd element:
[1, 2, 'a', 3, 4, 'a', 5, 6, 'a', 7, 8, 'a', 9, 0]
Insert b in the said list after 4 th element:
[1, 2, 3, 4, 'b', 5, 6, 7, 8, 'b', 9, 0]'''

def insert_element_at_nth_position(original_list, element, n):
    result = []
    for i, item in enumerate(original_list):
        result.append(item)
        if (i + 1) % n == 0:
            result.append(element)
    return result

original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
result_a = insert_element_at_nth_position(original_list, 'a', 2)
print("Insert 'a' after every 2nd element:")
print(result_a)
result_b = insert_element_at_nth_position(original_list, 'b', 4)
print("Insert 'b' after every 4th element:")
print(result_b)
