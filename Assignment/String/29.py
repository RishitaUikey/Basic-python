'''Write a Python program to set the indentation of the first line.'''
def set_first_line_indentation(text, indentation):
    lines = text.split('\n')
    lines[0] = indentation + lines[0]
    result = '\n'.join(lines)

    return result
text = """This is line 1.
This is line 2.
And this is line 3."""
indentation = "    " 
result = set_first_line_indentation(text, indentation)
print("Text with indentation set for the first line:")
print(result)
