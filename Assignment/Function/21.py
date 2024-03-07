'''Write a Python program that invokes a function after a specified period of time.
Sample Output:
Square root after specific miliseconds:
4.0
10.0
158.42979517754858'''

from time import sleep
import math

# Define a function named 'delay' that delays the execution of a function by the given milliseconds
def delay(fn, ms, *args):
    # Sleep for the specified number of milliseconds
    sleep(ms / 1000)
    
    # Call the provided function 'fn' with the given arguments '*args' and return the result
    return fn(*args)

# Print a message indicating the operation that follows
print("Square root after specific milliseconds:") 

# Call the 'delay' function with a lambda function to calculate square roots after specific delays
# Print the square root of 16 after a delay of 100 milliseconds
print(delay(lambda x: math.sqrt(x), 100, 16))

# Print the square root of 100 after a delay of 1000 milliseconds
print(delay(lambda x: math.sqrt(x), 1000, 100))

# Print the square root of 25100 after a delay of 2000 milliseconds
print(delay(lambda x: math.sqrt(x), 2000, 25100))
