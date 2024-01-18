'''
a = "STRING"
i = 0
while i < len(a):
    c = a[i]
    print(c)
    i = i + 1
'''
'''def search(char,str):
    L=len(str)
    print(L)
    i = 0
    while i < L:
        if str[i]== char:
            return 1
            i = i + 1
        return -1

print(search("N","PYTHON"))

'''

'''Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples.
Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]'''
'''from operator import intergetter
l = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
sorted_l=sorted(l,key=intergetter(-1))
print(sorted_l())'''

# Get user input for a list of numbers
numbers = int(input("Enter a list of numbers separated by spaces: "))

# Convert the input string to a list of integers
numbers_list = [int(x) for x in numbers.split()]

# Sort the list in ascending order
sorted_numbers = sorted(numbers_list)

# Print the sorted list
print("Numbers in ascending order:", sorted_numbers)


