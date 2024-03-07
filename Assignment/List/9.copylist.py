# Write a Python program to clone or copy a list.

org_list=[21,32,98,43]
clone_list=org_list[:]      # using slicing method
# clone_list=org_list.copy()   # using the copy method
print("Original list is: ",org_list)
print("The clone list is:",clone_list)