'''Write a  Python program to convert a hexadecimal color code to a tuple of integers corresponding to its RGB components.
Sample Output:
(255, 165, 1)
(255, 255, 255)
(0, 0, 0)
(255, 0, 0)
(0, 0, 128)
(192, 192, 192)'''

def hex_to_rgb(hex_code):
    hex_code = hex_code.lstrip('#')
    r = int(hex_code[0:2], 16)
    g = int(hex_code[2:4], 16)
    b = int(hex_code[4:6], 16)

    return (r, g, b)

def main():
    color_codes = [
        "#FFA501",
        "#FFFFFF",
        "#000000",
        "#FF0000",
        "#000080",
        "#C0C0C0"
    ]
    for code in color_codes:
        print(hex_to_rgb(code))

if __name__ == "__main__":
    main()
