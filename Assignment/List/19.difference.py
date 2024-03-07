# Write a Python program to calculate the difference between the two lists.

list1=[21,76,98,43,65]
list2=[12,34,65,84,93]
list=[]
for i in list1:
    if i not in list2:
        list.append(i)
for i in list2:
    if i not in list1:
        list.append(i)

print("the difference between the two lists: ",list)


