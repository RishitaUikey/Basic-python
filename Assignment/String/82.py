'''Write a  Python program to wrap a given string into a paragraph with a given width.
Sample Output:
Input a string: The quick brown fox.
Input the width of the paragraph: 10
Result:
The quick
brown fox.'''

def wrap_into_paragraph(input_string, width):
    words = input_string.split()
    paragraph = ""
    line_width = 0
    for word in words:
        if line_width + len(word) > width:
            paragraph += "\n" + word + " "
            line_width = len(word) + 1
        else:
            paragraph += word + " "
            line_width += len(word) + 1

    return paragraph.strip()
input_string = input("Input a string: ")
width = int(input("Input the width of the paragraph: "))
result = wrap_into_paragraph(input_string, width)
print("Result:")
print(result)
