'''Write a Python program to print the alphabet pattern 'Z'.
Expected Output:

*******                                                                 
     *                                                                  
    *                                                                   
   *                                                                    
  *                                                                     
 *                                                                      
*******   '''

for i in range(7):
    for j in range(7):
        if i==0:
            print("*",end="")
        elif i==1 and j==6:
            print("*",end="")
        elif i==2 and j==5:
            print("*",end="")
        elif i==3 and j==4:
            print("*",end="")
        elif i==4 and j==3:
            print("*",end="")
        elif i==5 and j==2:
            print("*",end="")
        elif i==6:
            print("*",end="")
        else:
            print(" ",end="")
    print()