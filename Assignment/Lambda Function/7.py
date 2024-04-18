'''Write a  Python program to find if a given string starts with a given character using Lambda.
Sample Output:
True
False'''

starts_with_char = lambda string, char: string.startswith(char)

string1 = "Python"
string2 = "Java"

char1 = "P"
char2 = "k"

result1 = starts_with_char(string1, char1)
result2 = starts_with_char(string2, char2)

print(result1)  
print(result2) 
