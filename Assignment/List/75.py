'''Write a Python program to create a list reflecting the run-length encoding from a given list of integers or a given list of characters.
Original list:
[1, 1, 2, 3, 4, 4.3, 5, 1]
List reflecting the run-length encoding from the said list:
[[2, 1], [1, 2], [1, 3], [1, 4], [1, 4.3], [1, 5], [1, 1]]
Original String:
automatically
List reflecting the run-length encoding from the said string:
[[1, 'a'], [1, 'u'], [1, 't'], [1, 'o'], [1, 'm'], [1, 'a'], [1, 't'], [1, 'i'], [1, 'c'], [1, 'a'], [2, 'l'], [1, 'y']]'''

original_list = [1, 1, 2, 3, 4, 4.3, 5, 1]
list = []
current_element = original_list[0]
count = 1
for i in range(1, len(original_list)):
    if original_list[i] == current_element:
        count += 1
    else:
        list.append([count, current_element])
        current_element = original_list[i]
        count = 1
list.append([count, current_element])
print("List reflecting the run-length encoding from the said list:", list)
