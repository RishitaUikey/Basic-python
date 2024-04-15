'''Write a Python program that uses the Sieve of Eratosthenes method to compute prime numbers 
up to a specified number.

Note: In mathematics, the sieve of Eratosthenes (Ancient Greek: κόσκινον Ἐρατοσθένους, kóskinon 
Eratosthénous), one of a number of prime number sieves, is a simple, ancient algorithm for 
finding all prime numbers up to any given limit.'''

def sieve_of_eratosthenes(limit):
    primes = [True] * (limit + 1)
    primes[0] = primes[1] = False  

    p = 2
    while p * p <= limit:
        if primes[p]:
            for i in range(p * p, limit + 1, p):
                primes[i] = False
        p += 1
    prime_numbers = [i for i in range(2, limit + 1) if primes[i]]
    return prime_numbers
limit = 50
print("Prime numbers up to", limit, "are:")
print(sieve_of_eratosthenes(limit))
