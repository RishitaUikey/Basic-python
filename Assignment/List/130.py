'''Write a  Python program to count the same pair in three given lists.
Original lists:
[1, 2, 3, 4, 5, 6, 7, 8]
[2, 2, 3, 1, 2, 6, 7, 9]
[2, 1, 3, 1, 2, 6, 7, 9]
Number of same pair of the said three given lists:
3'''

def count_same_pairs(list1, list2, list3):
    count = 0
    for i in range(len(list1)):
        if list1[i] == list2[i] and list2[i] == list3[i]:
            count += 1
    return count

list1 = [1, 2, 3, 4, 5, 6, 7, 8]
list2 = [2, 2, 3, 1, 2, 6, 7, 9]
list3 = [2, 1, 3, 1, 2, 6, 7, 9]

num_same_pairs = count_same_pairs(list1, list2, list3)

print("Original lists:")
print(list1)
print(list2)
print(list3)
print("Number of same pair of the said three given lists:", num_same_pairs)
