'''Write a Python program to print the alphabet pattern 'D'.
Expected Output:

 ****                                                                   
 *   *                                                                  
 *   *                                                                  
 *   *                                                                  
 *   *                                                                  
 *   *                                                                  
 ****    '''

for i in range(7):          # number of rows
    for j in range(5):       # number of coloumns
      
        if i==0 and (j==0 or j==1 or j==2 or j==3 ):
            print("*",end="")
        elif (i>0 and i<6) and (j==0  or j==4):
            print("*",end="")
        elif i==6 and (j==0 or j==1 or j==2 or j==3 ):
            print("*",end="")
        elif (i==0 and j==4) and (i==6 and j==4):
            print(" ",end="")
        else:
            print(" ",end=" ")
    print() 