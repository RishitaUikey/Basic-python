'''Write a  Python program to decapitalize the first letter of a given string.
Sample Output:
java Script'''
def decapitalize_first(input_str):
    decapitalized_str = input_str[0].lower() + input_str[1:]
    return decapitalized_str
def main():
    input_str = "Java Script"
    print(decapitalize_first(input_str))

if __name__ == "__main__":
    main()
