'''Write a Python program to convert the values of RGB components to a hexadecimal color code.
Sample Output:
FFA501
FFFFFF
000000
000080
C0C0C0'''
def rgb_to_hex(r, g, b):
    hex_r = format(r, '02x')
    hex_g = format(g, '02x')
    hex_b = format(b, '02x')
    hex_code = hex_r + hex_g + hex_b

    return hex_code.upper()

def main():
    colors = [
        (255, 165, 1),
        (255, 255, 255),
        (0, 0, 0),
        (0, 0, 128),
        (192, 192, 192)
    ]
    for color in colors:
        print(rgb_to_hex(*color))

if __name__ == "__main__":
    main()
