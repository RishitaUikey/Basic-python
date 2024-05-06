'''Write a Python program to convert a given string to Snake case.
Sample Output:
java_script
foo_bar
foo_bar
foo.bar
foo_bar
foo_bar
foo_bar'''

def to_snake_case(input_str):
    input_str = input_str.replace(' ', '_').replace('.', '_').replace('-', '_')
    snake_case_string = input_str.lower()

    return snake_case_string
def main():
    strings = [
        "java script",
        "foo Bar",
        "foo bar",
        "foo.Bar",
        "foo_bar",
        "foo-bar"
    ]
    for string in strings:
        print(to_snake_case(string))

if __name__ == "__main__":
    main()
