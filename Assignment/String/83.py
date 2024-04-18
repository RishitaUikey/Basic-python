'''Write a  Python program to print four integer values - decimal, octal, hexadecimal (capitalized), binary - in a single line.
Sample Output:
Input an integer: 25
Decimal Octal Hexadecimal (capitalized), Binary
25 31 19 11001'''

def print_integer_values(num):
    decimal = num
    octal = oct(num)[2:]
    hexadecimal = hex(num)[2:].upper()
    binary = bin(num)[2:]

    print("Decimal Octal Hexadecimal (capitalized) Binary")
    print("{: <8} {: <5} {: <22} {: <8}".format(decimal, octal, hexadecimal, binary))

num = int(input("Input an integer: "))
print_integer_values(num)
