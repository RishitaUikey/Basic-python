'''Write a Python program to print the square and cube symbols in the area of a rectangle and the volume of a cylinder.
Sample output:
The area of the rectangle is 1256.66cm2
The volume of the cylinder is 1254.725cm3'''

def print_area_and_volume(area, volume):
    formatted_area = "{:.2f} \u33A1".format(area)
    formatted_volume = "{:.3f} \u33A5".format(volume)
    print("The area of the rectangle is", formatted_area)
    print("The volume of the cylinder is", formatted_volume)
area_rectangle = 1256.66
volume_cylinder = 1254.725
print_area_and_volume(area_rectangle, volume_cylinder)
