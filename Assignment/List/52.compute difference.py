'''Write a Python program to compute the difference between two lists.
Sample data: ["red", "orange", "green", "blue", "white"], ["black", "yellow", "green", "blue"]
Expected Output:
Color1-Color2: ['white', 'orange', 'red']
Color2-Color1: ['black', 'yellow']
'''

list_1=["red", "orange", "green", "blue", "white"]
list_2=["black", "yellow", "green", "blue"]

color1_color2=[color for color in list_1 if color not in list_2]
color2_color1=[color for color in list_2 if color not in list_1]

print("Color1-Color2:",color1_color2)
print("Color2-Color1:",color2_color1)