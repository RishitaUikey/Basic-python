'''Write a  Python program to convert a given string to Camelcase.
Sample Output:
javascript
fooBar
fooBar
foo.Bar
fooBar
foobar
fooBar
'''
def to_camel_case(input_str):
    words = input_str.split()
    camel_case_words = [words[0].lower()] + [word.capitalize() for word in words[1:]]
    camel_case_string = ''.join(camel_case_words)

    return camel_case_string
def main():
    strings = [
        "javascript",
        "foo Bar",
        "foo bar",
        "foo.Bar",
        "foo_bar",
        "foo-bar"
    ]
    for string in strings:
        print(to_camel_case(string))

if __name__ == "__main__":
    main()
