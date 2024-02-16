'''Write a Python program to print the alphabet pattern 'T'.
Expected Output:
 *****                                                                  
   *                                                                    
   *                                                                    
   *                                                                    
   *                                                                    
   *                                                                    
   *  '''

for i in range(7):
    for j in range(5):
        if i==0 :
            print("*",end="")
        elif (i>0 and i<7) and j==2:
            print("*",end="")
        elif (i==0 or i==2) or (j==0 or j==1 or j==3 or j==3):
            print(" ",end="")
    print()
