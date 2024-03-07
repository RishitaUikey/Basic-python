'''Write a Python function to multiply all the numbers in a list.
Sample List : (8, 2, 3, -1, 7)
Expected Output : -336  '''

def multiply_all(slist):

    result = 1
    for i in slist:
        result *= i
    return result
list1 = [8,2,3,-1,7]
mul_all = multiply_all(list1)
print("Multiply all the numbers in a list: ",mul_all)