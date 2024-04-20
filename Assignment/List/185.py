'''Write a  Python program to convert a given decimal number to a binary list.
Original Number: 8
Decimal number ( 8 ) to binary list:
[1, 0, 0, 0]
Original Number: 45
Decimal number ( 45 ) to binary list:
[1, 0, 1, 1, 0, 1]
Original Number: 100
Decimal number ( 100 ) to binary list:
[1, 1, 0, 0, 1, 0, 0]'''

def decimal_to_binary_list(decimal):
    binary_list = []
    while decimal > 0:
        binary_list.append(decimal % 2)
        decimal //= 2
    binary_list.reverse()
    return binary_list

numbers = [8, 45, 100]
for number in numbers:
    binary_list = decimal_to_binary_list(number)
    print("Original Number:", number)
    print("Decimal number (", number, ") to binary list:")
    print(binary_list)
