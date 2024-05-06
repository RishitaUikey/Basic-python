'''Write a  Python program to remove existing indentation from all of the lines in a given text.'''
def remove_indentation(text):
    lines = text.split('\n')
    dedented_lines = [line.lstrip() for line in lines]
    dedented_text = '\n'.join(dedented_lines)

    return dedented_text
indented_text = """
    aaaaaaa ddddd ffff 
     jjjjj ttttt rrrr 
        gggg iiii rdesw
    """
result = remove_indentation(indented_text)

print("Original text:")
print(indented_text)
print("\nText after removing indentation:")
print(result)
