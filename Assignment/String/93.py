'''Write a Python program to extract numbers from a given string.
Sample Output:
Original string: red 12 black 45 green
Extract numbers from the said string: [12, 45]'''
def extract_numbers(input_str):
    num_str = ''
    numbers = []
    for char in input_str:
        if char.isdigit():
            num_str += char
        elif num_str:
            numbers.append(int(num_str))
            num_str = ''  
    if num_str:
        numbers.append(int(num_str))
    return numbers

def main():
    input_str = "red 12 black 45 green"
    print("Original string:")
    print(input_str)
    print("Extract numbers from the said string:")
    print(extract_numbers(input_str))

if __name__ == "__main__":
    main()
