'''Write a Python program to guess a number between 1 and 9.
Note : User is prompted to enter a guess. If the user guesses
wrong then the prompt appears again until the guess is correct, 
on successful guess, user will get a "Well guessed!" message, 
and the program will exit.'''

import random

# Generate a random number between 1 and 9
target_number = random.randint(1, 9)

while True:
    # Prompt the user to enter a guess
    guess = int(input("Guess a number between 1 and 9: "))
    
    # Check if the guess is correct
    if guess == target_number:
        print("Well guessed!")
        break
    else:
        print("Wrong guess. Try again.")
