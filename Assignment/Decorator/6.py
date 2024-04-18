# Write a Python program that implements a decorator to retry a function multiple times in case of failure.

import time

def retry_on_failure(max_retries, delay=1):
    def decorator(func):
        def wrapper(*args, **kwargs):
            retries = 0
            while retries < max_retries:
                try:
                    result = func(*args, **kwargs)
                    return result
                except Exception as e:
                    print(f"Retry {retries + 1}/{max_retries}: {e}")
                    retries += 1
                    time.sleep(delay)
            raise Exception("Maximum retries exceeded")
        return wrapper
    return decorator

@retry_on_failure(max_retries=3, delay=1)
def maybe_fails():
    import random
    if random.random() < 0.3:
        raise ValueError("Something went wrong")
    else:
        return "Success"

try:
    result = maybe_fails()
    print("Result:", result)
except Exception as e:
    print("Error:", e)
