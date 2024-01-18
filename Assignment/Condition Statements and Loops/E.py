'''Write a Python program to print the alphabet pattern 'E'.
Expected Output:

 *****                                                                  
 *                                                                      
 *                                                                      
 ****                                                                   
 *                                                                      
 *                                                                      
 *****   '''

for i in range(7):
    for j in range(5):
        if i==0:
            print("*",end="")
        elif i==3 and (j>0 and j<4):
            print("*",end="")
        elif i>0 and i<7 and j==0 :
            print("*",end="")
        elif i==6:
            print("*",end="")
        else:
            print(" ",end=" ")
    print()