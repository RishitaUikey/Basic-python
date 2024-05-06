# Write a Python program to get the frequency of elements in a list.

my_list=[12,32,34,54,65,12,78,93,32,65]
frequency_dict={}

for i in my_list:
    if i in frequency_dict:
        frequency_dict[i]+=1
    else:
        frequency_dict[i]=1

for element, frequency in frequency_dict.items():
    print(f"Element {element} occurs {frequency} times")

