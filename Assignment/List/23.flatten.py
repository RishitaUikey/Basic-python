# Write a Python program to flatten a shallow list.

s_list = [[1, 2, 3], [4, 5], [6, 7, 8]]
flatten_list=[]

for sublist in s_list:
    for i in sublist:
        flatten_list.append(i)

print("flatten a shallow list:",flatten_list)