# Write a Python program to find the two numbers whose product is maximum among all the pairs in a given list of numbers. Use the Python set.

numbers = [1, 3, 5, 2, 8, 10, 6, 4, 9]
max_num = float('-inf')
second_max_num = float('-inf')

for num in numbers:
    if num > max_num:
        second_max_num = max_num
        max_num = num
    elif num > second_max_num:
        second_max_num = num

max_product = max_num * second_max_num

print("The two numbers whose product is maximum among all pairs are:", max_num, "and", second_max_num)
print("Maximum product:", max_product)
