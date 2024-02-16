'''Write a Python program to print the following patterns.
Expected Output:

  ****                                                                  
 *                                                                      
 *                                                                      
  ***                                                                   
     *                                                                  
     *                                                                  
 **** '''

for i in range(7):
    for j in range(5):
        if i==0 and (j==1 or j==2 or j==3 or j==4):
            print("*", end="")
        elif i==0 and j==0:
            print(" ",end="")
        elif (i==1 or i==2) and j==0:
            print("*", end="")
        elif i==3 and (j==1 or j==2 or j==3 ):
            print("*", end="")
        elif i==3 and j==0:
            print(" ",end="")
        elif (i==4 or i==5) and j==4:
            print("*", end="")
        elif (i==4 or i==5) and (j==0 or j==1 or j==2 or j==3):
            print(" ", end="")
        elif i==6 and (j==0 or j==1 or j==2 or j==3):
            print("*", end="")
        else :
            print("",end="")
    print()