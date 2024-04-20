'''Write a  Python program to compute the average of the n-th element in a given list of lists with different lengths.
Original list:
[[0, 1, 2], [2, 3, 4], [3, 4, 5, 6], [7, 8, 9, 10, 11], [12, 13, 14]]
Average of n-th elements in the said list of lists with different lengths:
[4.8, 5.8, 6.8, 8.0, 11.0]'''

def average_nth_element(list_of_lists, n):
    sum_n = 0
    count = 0
    for sublist in list_of_lists:
        if len(sublist) > n:
            sum_n += sublist[n]
            count += 1
    if count == 0:
        return "No elements found at index " + str(n)
    else:
        return sum_n / count

original_list = [[0, 1, 2], [2, 3, 4], [3, 4, 5, 6], [7, 8, 9, 10, 11], [12, 13, 14]]
n = 2  
result = average_nth_element(original_list, n)

print("Original list:")
print(original_list)
print("Average of the {}-th elements in the said list of lists with different lengths:".format(n))
print(result)
