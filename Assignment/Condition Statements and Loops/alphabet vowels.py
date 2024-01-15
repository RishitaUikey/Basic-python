'''Write a Python program to check whether an alphabet is a vowel or consonant.
Expected Output:

Input a letter of the alphabet: k                                       
k is a consonant.'''

x=str(input("Enter the alphabet: "))
y='aeiouAEIOU'
for i in x:
    if(i in y):
        print(i,"=vowels")
    if( i not in y):
        print(i,"=consonent")