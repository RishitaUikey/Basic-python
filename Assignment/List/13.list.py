# 13. Write a Python program to generate a 3*4*6 3D array whose each element is *.

array_3d = [[['*' for _ in range(6)] for _ in range(4)] for _ in range(3)]
for layer in array_3d:
    for row in layer:
        print(row)
    print()  
