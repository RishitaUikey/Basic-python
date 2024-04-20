'''Write a  Python program to sort a list of lists by a given index of the inner list.
Original list:
[('Greyson Fulton', 98, 99), ('Brady Kent', 97, 96), ('Wyatt Knott', 91, 94), ('Beau Turnbull', 94, 98)]
Sort the said list of lists by a given index ( Index = 0 ) of the inner list
[('Beau Turnbull', 94, 98), ('Brady Kent', 97, 96), ('Greyson Fulton', 98, 99), ('Wyatt Knott', 91, 94)]
Sort the said list of lists by a given index ( Index = 2 ) of the inner list
[('Wyatt Knott', 91, 94), ('Brady Kent', 97, 96), ('Beau Turnbull', 94, 98), ('Greyson Fulton', 98, 99)]'''

def sort_list_of_lists(lst, index):
    return sorted(lst, key=lambda x: x[index])

original_list = [('Greyson Fulton', 98, 99), ('Brady Kent', 97, 96), ('Wyatt Knott', 91, 94), ('Beau Turnbull', 94, 98)]
sorted_list_index_0 = sort_list_of_lists(original_list, 0)
sorted_list_index_2 = sort_list_of_lists(original_list, 2)
print("Original list:")
print(original_list)
print("Sort the said list of lists by a given index ( Index = 0 ) of the inner list")
print(sorted_list_index_0)
print("Sort the said list of lists by a given index ( Index = 2 ) of the inner list")
print(sorted_list_index_2)
