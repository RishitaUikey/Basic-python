'''Write a  Python program to remove the first specified number of elements from a given list satisfying a condition.
Remove the first 4 number of even numbers from the following list:
[3,10,4,7,5,7,8,3,3,4,5,9,3,4,9,8,5]
Output:
[3, 7, 5, 7, 3, 3, 5, 9, 3, 4, 9, 8, 5]
Original list:
[3, 10, 4, 7, 5, 7, 8, 3, 3, 4, 5, 9, 3, 4, 9, 8, 5]
Remove first 4 even numbers from the said list:
[3, 7, 5, 7, 3, 3, 5, 9, 3, 4, 9, 8, 5]'''

def remove_first_n_elements(condition, n, lst):
    count = 0
    new_lst = []
    for item in lst:
        if condition(item):
            count += 1
            if count <= n:
                continue
        new_lst.append(item)
    return new_lst

original_list = [3, 10, 4, 7, 5, 7, 8, 3, 3, 4, 5, 9, 3, 4, 9, 8, 5]
print("Original list:")
print(original_list)

new_list = remove_first_n_elements(lambda x: x % 2 == 0, 4, original_list)
print("Remove first 4 even numbers from the said list:")
print(new_list)
