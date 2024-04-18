'''Write a  Python program to convert a given list of tuples to a list of lists.
Original list of tuples: [(1, 2), (2, 3), (3, 4)]
Convert the said list of tuples to a list of lists: [[1, 2], [2, 3], [3, 4]]
Original list of tuples: [(1, 2), (2, 3, 5), (3, 4), (2, 3, 4, 2)]
Convert the said list of tuples to a list of lists: [[1, 2], [2, 3, 5], [3, 4], [2, 3, 4, 2]]'''

t = [(1, 2), (2, 3), (3, 4)]
list_of_lists = [list(t) for t in t]
print("Convert the said list of tuples to a list of lists:",list_of_lists)
list_of_tuples = [(1, 2), (2, 3, 5), (3, 4), (2, 3, 4, 2)]
list_of_lists = [list(t) for t in list_of_tuples]
print("\nOriginal list of tuples:")
print(list_of_tuples)
print("Convert the said list of tuples to a list of lists:")
print(list_of_lists)
