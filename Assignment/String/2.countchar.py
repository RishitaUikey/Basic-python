'''Write a Python program to count the number of 
characters (character frequency) in a string.
Sample String : google.com'
Expected Result : {'g': 2, 'o': 3, 'l': 1, 'e': 1, '.': 1, 'c': 1, 'm': 1}'''

given_string = 'google.com'
frequency={}
for i in given_string:
    if i in frequency:
        frequency[i]+=1
    else:
        frequency[i] = 1

print(frequency)


