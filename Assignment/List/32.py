# Write a Python program to check whether a list contains a sublist.

def is_sublist(main_list, sublist):
    for i in range(len(main_list)):
        if main_list[i:i+len(sublist)] == sublist:
            return True
    return False

print(is_sublist([1, 2, 3, 4, 5], [2, 3]))       
print(is_sublist([1, 2, 3, 4, 5], [5, 6]))       
print(is_sublist(['a', 'b', 'c', 'd'], ['c', 'a']))  
