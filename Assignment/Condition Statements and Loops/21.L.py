'''Write a Python program to print the alphabet pattern 'L'.
Expected Output:

 *                                                                      
 *                                                                      
 *                                                                      
 *                                                                      
 *                                                                      
 *                                                                      
 *****   '''

for i in range(7):
    for j in range(5):
        if (i>=0 and i<7) and j==0:
            print("*",end="")
        if i==6 and (j>=0 and j<5):
            print("*",end="")
        else:
            print("",end="")
    print()