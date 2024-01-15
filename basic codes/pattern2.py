'''Write a Python program to construct the following pattern, using a nested for loop.
*
* *
* * *
* * * *
* * * * *  '''
for i in range(1,6):
    for j in range(1,i+1):
        print(" * ",end="")
    print()