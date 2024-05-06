'''Write a Python program to check if each number is prime in a given list of numbers.
Return True if all numbers are prime otherwise False.
Sample Data:
([0, 3, 4, 7, 9]) -> False
([3, 5, 7, 13]) -> True
([1, 5, 3]) -> False '''

def are_all_primes(numbers):
    for number in numbers:
        if number <= 1:
            return False
        if number <= 3:
            continue
        if number % 2 == 0 or number % 3 == 0:
            return False
        i = 5
        while i * i <= number:
            if number % i == 0 or number % (i + 2) == 0:
                return False
            i += 6
    return True
print(are_all_primes([0, 3, 4, 7, 9]))  
print(are_all_primes([3, 5, 7, 13]))    
print(are_all_primes([1, 5, 3]))        
