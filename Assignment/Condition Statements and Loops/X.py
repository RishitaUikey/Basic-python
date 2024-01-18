'''Write a Python program to print the alphabet pattern 'X'.
Expected Output:

 *   *                                                                  
 *   *                                                                  
  * *                                                                   
   *                                                                    
  * *                                                                   
 *   *                                                                  
 *   *  '''

for i in range(7):
    for j in range(5):    
        if (i==0 or i==1 or i==5 or i==6) and (j==0 or j==4):
            print("*",end="")
        elif (i==0 or i==1 or i==5 or i==6) and (j==1 or j==2 or j==3):
            print(" ",end="")
        elif (i==2 or i==4) and (j==1 or j==3):
            print("*",end="")
        elif (i==2 or i==4) and (j==0 or j==2 or j==4):
            print(" ",end="")
        elif i==3 and j==2:
            print("*",end="")
        elif i==3 and (j==0 or j==1 or j==3 or j==4):
            print(" ",end="")
    print()