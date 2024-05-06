''' Write a Python program to move all spaces to the front of a given string in a single traversal.'''

def move_spaces_to_front(input_string):
    char_list = list(input_string)
    length = len(char_list)
    next_space = 0
    for i in range(length):
        if char_list[i] == ' ':
            char_list[next_space], char_list[i] = char_list[i], char_list[next_space]
            next_space += 1
    result = ''.join(char_list)
    return result
input_string = "move all spaces to the front"
result = move_spaces_to_front(input_string)
print("String with spaces moved to the front:", result)
