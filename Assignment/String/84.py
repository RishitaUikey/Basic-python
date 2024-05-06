'''Write a Python program to swap cases in a given string.
Sample Output:
 pYTHON eXERCISES
jAVA
nUMpY'''
def swap_case(input_string):
    return input_string.swapcase()
input_string1 = "Python Exercises"
input_string2 = "Java"
input_string3 = "NumPy"

result1 = swap_case(input_string1)
result2 = swap_case(input_string2)
result3 = swap_case(input_string3)

print(result1)
print(result2)
print(result3)
