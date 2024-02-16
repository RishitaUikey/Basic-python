# Write a Python program to create a decorator to convert the return value of a function to a specified data type.

def fun(a):
    def wrap(*args, **kwargs):
        print("argument",*args, **kwargs)
        result = a(*args, **kwargs)
        # return result
        print('result : ', result, 'converted to str: ', str(result), 'new type : ', type(str(result)))
    return wrap
@fun
def mul(x, y):
    return x * y
result = mul(10, 20)
# print("Result:", result, type(result))



