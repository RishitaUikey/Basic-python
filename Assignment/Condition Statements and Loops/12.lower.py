'''Write a Python program that accepts a sequence of lines (blank line to terminate) as input and prints 
the lines as output (all characters in lower case).'''

while True:
    x = input("Enter the input (blank line to terminate): ")
    if x:
        print(x.lower())
    else:
        break
