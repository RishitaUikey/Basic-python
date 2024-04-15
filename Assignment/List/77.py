'''Write a Python program to decode a run-length message.
Original encoded list:
[[2, 1], 2, 3, [2, 4], 5, 1]
Decode a run-length encoded said list:
[1, 1, 2, 3, 4, 4, 5, 1]
'''

encoded_list = [[2, 1], 2, 3, [2, 4], 5, 1]
decoded_list = []
for item in encoded_list:
    if isinstance(item, list):
        count, value = item
        decoded_list.extend([value] * count)
    else:
        decoded_list.append(item)
print("Decode a run-length encoded said list:", decoded_list)