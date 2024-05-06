'''Write a Python program to add prefix text to all of the lines in a string'''
def add_prefix(text, prefix):
    result = prefix + text.replace('\n', '\n' + prefix)
    return result
text = """This is line 1.
This is line 2.
And this is line 3."""
prefix = "Prefix: "
result = add_prefix(text, prefix)
print("Text after adding prefix to each line:")
print(result)
