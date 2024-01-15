# check vowels in a string
a = (str(input("Enter the Name = ")))
b = 'aeiouAEIOU'
for i in a:
    if i in b :
        print(i,"=vowels")
    if i not in b:
        print(i,"=consonent")
        
    

    