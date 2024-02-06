# Write a Python program to count the occurrences of each word in a given sentence.

given_string = 'she is the only girl who is the brand ambassador of the company.'
count_words = {}
words = given_string.split()
for word in words:
    if word in count_words:
        count_words[word] += 1
    else :
        count_words[word] = 1
print(count_words) 

