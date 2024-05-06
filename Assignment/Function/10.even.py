'''Write a Python program to print the even numbers from a given list.
Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9]
Expected Result : [2, 4, 6, 8]  '''

def even_number(my_list):
    even_numbers = [num for num in my_list if num % 2 == 0]
    return even_numbers
sample_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
result = even_number(sample_list)
print("Expected Result:", result)
