'''Write a Python program to remove a specific item from a given list of lists.
Original list of lists:
[['Red', 'Maroon', 'Yellow', 'Olive'], ['#FF0000', '#800000', '#FFFF00', '#808000'], ['rgb(255,0,0)', 'rgb(128,0,0)', 'rgb(255,255,0)', 'rgb(128,128,0)']]
Remove 1st list from the saod given list of lists:
[['Maroon', 'Yellow', 'Olive'], ['#800000', '#FFFF00', '#808000'], ['rgb(128,0,0)', 'rgb(255,255,0)', 'rgb(128,128,0)']]
Remove 2nd list from the saod given list of lists:
[['Red', 'Yellow', 'Olive'], ['#FF0000', '#FFFF00', '#808000'], ['rgb(255,0,0)', 'rgb(255,255,0)', 'rgb(128,128,0)']]
Remove 4th list from the saod given list of lists:
[['Red', 'Maroon', 'Yellow'], ['#FF0000', '#800000', '#FFFF00'], ['rgb(255,0,0)', 'rgb(128,0,0)', 'rgb(255,255,0)']]'''

def remove_list(original_lists, index):
    if index < len(original_lists):
        del original_lists[index]
    return original_lists

original_list_of_lists = [['Red', 'Maroon', 'Yellow', 'Olive'], ['#FF0000', '#800000', '#FFFF00', '#808000'], ['rgb(255,0,0)', 'rgb(128,0,0)', 'rgb(255,255,0)', 'rgb(128,128,0)']]
removed_first_list = remove_list(original_list_of_lists.copy(), 0)
removed_second_list = remove_list(original_list_of_lists.copy(), 1)
removed_fourth_list = remove_list(original_list_of_lists.copy(), 3)
print("Remove 1st list from the given list of lists:")
print(removed_first_list)
print("Remove 2nd list from the given list of lists:")
print(removed_second_list)
print("Remove 4th list from the given list of lists:")
print(removed_fourth_list)
