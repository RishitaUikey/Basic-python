'''. Write a Python program to check whether all dictionaries in a list are empty or not.
Sample list : [{},{},{}]
Return value : True
Sample list : [{1,2},{},{}]
Return value : False'''

sample_list1 = [{}, {}, {}]
sample_list2 = [{1, 2}, {}, {}]
empty1 = all(not bool(d) for d in sample_list1)
empty2 = all(not bool(d) for d in sample_list2)
print("Return value for sample list 1:", empty1)
print("Return value for sample list 2:", empty2)
