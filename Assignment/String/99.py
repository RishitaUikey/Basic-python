'''Write a Python program to split a multi-line string into a list of lines.
Sample Output:
Original string: This
is a
multiline
string.
Split the said multiline string into a list of lines:
['This', 'is a', 'multiline', 'string.', '']'''

def split_into_lines(input_str):
    # Split the string into a list of lines
    lines = input_str.splitlines()
    return lines

# Sample usage
def main():
    input_str = """This
is a
multiline
string."""
    print("Original string:")
    print(input_str)
    print("Split the said multiline string into a list of lines:")
    print(split_into_lines(input_str))

if __name__ == "__main__":
    main()
