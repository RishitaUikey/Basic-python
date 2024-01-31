'''Write a Python program to check if each number is prime in a given list of numbers. 
Return True if all numbers are prime otherwise False.
Sample Data:
([0, 3, 4, 7, 9]) -> False
([3, 5, 7, 13]) -> True
([1, 5, 3]) -> False'''


input_list = input("Enter the list of numbers separated by commas: ").split(',')
numbers = [int(x) for x in input_list]

all_prime = True 

for num in numbers:
    if num <= 1:
        all_prime = False  
        break
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            all_prime = False  
            break

if all_prime:
    print(input_list,"True")
else:
    print(input_list,"False")
