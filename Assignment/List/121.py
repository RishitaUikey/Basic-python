''' Write a  Python program to find nested list elements that are present in another list.
Original lists:
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
[[12, 18, 23, 25, 45], [7, 11, 19, 24, 28], [1, 5, 8, 18, 15, 16]]
Intersection of said nested lists:
[[12], [7, 11], [1, 5, 8]]'''

def find_intersection(main_list, nested_list):
    intersection = []
    for sublist in nested_list:
        intersecting_elements = [item for item in sublist if item in main_list]
        intersection.append(intersecting_elements)
    return intersection

main_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
nested_list = [[12, 18, 23, 25, 45], [7, 11, 19, 24, 28], [1, 5, 8, 18, 15, 16]]

intersection = find_intersection(main_list, nested_list)

print("Original lists:")
print(main_list)
print(nested_list)
print("Intersection of said nested lists:")
print(intersection)
