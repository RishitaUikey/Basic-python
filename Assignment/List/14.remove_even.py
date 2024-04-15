# Write a Python program to print the numbers of a specified list after removing even numbers from it.

list=[37,12,59,63,48,93,74]
new_list=[]
for i in list:
    if i%2!=0:
        new_list.append(i)
print("the numbers of a specified list after removing even numbers from it is: ",new_list)
    