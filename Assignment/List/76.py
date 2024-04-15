'''Write a Python program to create a list reflecting the modified run-length encoding from a given list of integers or a given list of characters.
Original list:
[1, 1, 2, 3, 4, 4, 5, 1]
List reflecting the modified run-length encoding from the said list:
[[2, 1], 2, 3, [2, 4], 5, 1]
Original String:
aabcddddadnss
List reflecting the modified run-length encoding from the said string:
[[2, 'a'], 'b', 'c', [4, 'd'], 'a', 'd', 'n', [2, 's']]'''

original_list = [1, 1, 2, 3, 4, 4, 5, 1]
encoded_list = []
current_element = original_list[0]
count = 1
for i in range(1, len(original_list)):
    if original_list[i] == current_element:
        count += 1
    else:
        if count == 1:
            encoded_list.append(current_element)
        else:
            encoded_list.append([count, current_element])
        current_element = original_list[i]
        count = 1
if count == 1:
    encoded_list.append(current_element)
else:
    encoded_list.append([count, current_element])

print("List reflecting the modified run-length encoding from the said list:", encoded_list)

original_string = "aabcddddadnss"
original_list_str = list(original_string)
encoded_list_str = []
current_element = original_list_str[0]
count = 1

for i in range(1, len(original_list_str)):
    if original_list_str[i] == current_element:
        count += 1
    else:
        if count == 1:
            encoded_list_str.append(current_element)
        else:
            encoded_list_str.append([count, current_element])
        current_element = original_list_str[i]
        count = 1
if count == 1:
    encoded_list_str.append(current_element)
else:
    encoded_list_str.append([count, current_element])
print("List reflecting the modified run-length encoding from the said string:", encoded_list_str)