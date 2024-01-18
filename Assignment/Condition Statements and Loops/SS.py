'''Write a Python program to print the following patterns.
Expected Output:

ooooooooooooooooo                                                       
ooooooooooooooooo                                                       
ooooooooooooooooo                                                       
oooo                                                                    
oooo                                                                    
oooo                                                                    
ooooooooooooooooo                                                       
ooooooooooooooooo                                                       
ooooooooooooooooo                                                       
             oooo                                                       
             oooo                                                       
             oooo                                                       
ooooooooooooooooo                                                       
ooooooooooooooooo                                                       
ooooooooooooooooo '''

for i in range(15):
    for j in range(17):
        if i==0 or i==1 or i==2:
            print("o",end="")
        elif (i==3 or i==4 or i==5) and (j==0 or j==1 or j==2 or j==3):
            print("o",end="")
        elif i==6 or i==7 or i==8:
            print("o",end="")
        elif (i==9 or i==10 or i==11) and (j==13 or j==14 or j==15 or j==16):
            print("o",end="")
        elif (i==9 or i==10 or i==11) and (j==0 or j==1 or j==2 or j==3 or j==4 \
        or j==5 or j==6 or j==7 or j==8 or j==9 or j==10 or j==11 or j==12):
            print(" ",end="")
        if i==12 or i==13 or i==14:
            print("o",end="")
    print()