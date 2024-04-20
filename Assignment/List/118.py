''' Write a  Python program to find the difference between elements (n+1th - nth) of a given list of numeric values.
Original list:
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Dfference between elements (n+1th - nth) of the said list :
[1, 1, 1, 1, 1, 1, 1, 1, 1]
Original list:
[2, 4, 6, 8]
Dfference between elements (n+1th - nth) of the said list :
[2, 2, 2]'''

def calculate_differences(lst):
    differences = [lst[i+1] - lst[i] for i in range(len(lst)-1)]
    return differences

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2 = [2, 4, 6, 8]

diff1 = calculate_differences(list1)
diff2 = calculate_differences(list2)

print("Original list:")
print(list1)
print("Difference between elements (n+1th - nth) of the said list:")
print(diff1)
print("Original list:")
print(list2)
print("Difference between elements (n+1th - nth) of the said list:")
print(diff2)
