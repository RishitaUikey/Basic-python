'''Write a Python program to print the alphabet pattern 'O'.
Expected Output:

  ***                                                                   
 *   *                                                                  
 *   *                                                                  
 *   *                                                                  
 *   *                                                                  
 *   *                                                                  
  ***    '''

for i in range(7):
    for j in range(5):
        if i==0 and (j==1 or j==2 or j==3):
            print("*",end=" ")
        elif i==0  and (j==0 or j==4):
            print(" ",end=" ")
        elif (i>0 and i<6) and (j==0 or j==4):
            print("*",end=" ")
        elif i==6 and (j==1 or j==2 or j==3):
            print("*",end=" ")
        elif i==6 and (j==0 or j==4):
            print(" ",end=" ")    
        else:
            print(" ",end=" ")
    print()
