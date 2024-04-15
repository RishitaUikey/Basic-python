# Write a Python program to find the list of words that are longer than n from a given list of words.

list=['Rishita','Dhrishti','Shruti','Sejal','Renu','Neha']
n=int(input("Enter a number:"))
long_words=[]
for i in list:
    if len(i) > n:
        long_words.append(i)
        
print("the list of words that are longer than ",n," from a given list of words are :",long_words)
