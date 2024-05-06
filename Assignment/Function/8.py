'''Write a Python function that takes a list and returns a new list with distinct elements from the first list.
Sample List : [1,2,3,3,3,3,4,5]
Unique List : [1, 2, 3, 4, 5]'''

def modify(sample_list):
    unique_list = list(set(sample_list))
    return unique_list
my_list = [1,2,3,3,3,3,4,5]
new_list = modify(my_list)   
print("New list: ",new_list)


   