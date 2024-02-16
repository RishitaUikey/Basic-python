'''Write a Python program to print the alphabet pattern 'M'.
Expected Output:

  *       *                                                             
  *       *                                                             
  * *   * *                                                             
  *   *   *                                                             
  *       *                                                             
  *       *                                                             
  *       *   '''


for i in range(7):
    for j in range(5):
        if j == 0 or j == 4 or (i == 2 and (j == 1 or j == 3)) or (i == 3 and j == 2):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()



