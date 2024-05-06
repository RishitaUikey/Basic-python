# Write a Python program that prompts the user to input an integer and raises a 
# ValueError exception if the input is not a valid integer.

def get_integer_input(prompt):
    while True:
        try:
            user_input = input(prompt)
            integer = int(user_input)
            return integer
        except ValueError:
            print("Error: Please enter a valid integer.")

try:
    user_integer = get_integer_input("Enter an integer: ")
    print("Input integer:", user_integer)
except ValueError:
    print("Error occurred while getting integer input.")
