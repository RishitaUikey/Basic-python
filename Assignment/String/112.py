'''Write a Python program to calculate the sum of two numbers given as strings. Return the result in the same string representation.
Sample Data:
( "234242342341", "2432342342") -> "236674684683"
( "", "2432342342") -> False ( "1000", "0") -> "1000"
( "1000", "10") -> "1010"
'''
def sum_of_strings(str1, str2):
    if not str1 or not str2:
        return False
    try:
        result = str(int(str1) + int(str2))
    except ValueError:
        return False
    
    return result
samples = [
    ("234242342341", "2432342342"),
    ("", "2432342342"),
    ("1000", "0"),
    ("1000", "10")
]
for str1, str2 in samples:
    result = sum_of_strings(str1, str2)
    print(f'("{str1}", "{str2}") -> {result if result else "False"}')
