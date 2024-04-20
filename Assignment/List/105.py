'''Write a  Python program to compute average of two given lists.
Original list:
[1, 1, 3, 4, 4, 5, 6, 7]
[0, 1, 2, 3, 4, 4, 5, 7, 8]
Average of two lists:
3.823529411764706'''

def average_of_lists(list1, list2):
    sum_list = [x + y for x, y in zip(list1, list2)]
    return sum(sum_list) / len(sum_list)
original_list1 = [1, 1, 3, 4, 4, 5, 6, 7]
original_list2 = [0, 1, 2, 3, 4, 4, 5, 7, 8]
average = average_of_lists(original_list1, original_list2)
print("Original list:")
print(original_list1)
print(original_list2)
print("Average of two lists:")
print(average)
