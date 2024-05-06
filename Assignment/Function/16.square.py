# Write a Python function to create and print a list where the values are the squares of numbers between 1 and 30 (both included).

def square_of_numbers():
    square_list = []
    for i in range(1,31):
        square = i**2
        square_list.append(square)
    return square_list
output = square_of_numbers()
print(output)