# Write a  Python program to create a decorator function to measure the execution time of a function.

import time

def measure_execution_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Function '{func.__name__}' executed in {execution_time:.6f} seconds")
        return result
    return wrapper

@measure_execution_time
def some_function():
    time.sleep(2)  

some_function()
