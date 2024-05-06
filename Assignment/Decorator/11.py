# Write a Python program that implements a decorator to measure the memory usage of a function.

import psutil
import functools

def measure_memory_usage(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        process = psutil.Process()
        before_memory = process.memory_info().rss
        result = func(*args, **kwargs)
        after_memory = process.memory_info().rss
        memory_usage = (after_memory - before_memory) / (1024 * 1024)  # Convert to MiB
        print(f"Memory usage of '{func.__name__}': {memory_usage:.2f} MiB")
        return result
    return wrapper

@measure_memory_usage
def some_function():
    data = [i for i in range(1000000)]
    return data

result = some_function()
