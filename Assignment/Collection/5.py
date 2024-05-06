'''Write a  Python program that accepts some words and counts the number of distinct words. Print the number of distinct words and the number of occurrences of each distinct word according to their appearance.
Input number of words: 5
Input the words:
Red
Green
Blue
Black
White
5
1 1 1 1 1'''

def count_distinct_words(num_words):
    word_counts = {}
    distinct_words = []

    for i in range(num_words):
        word = input("Enter word {}: ".format(i + 1))
        if word not in word_counts:
            distinct_words.append(word)
        word_counts[word] = word_counts.get(word, 0) + 1

    print("Number of distinct words:", len(distinct_words))
   
    for word in distinct_words:
        print(word, "-", word_counts[word])

num_words = int(input("Enter the number of words: "))

count_distinct_words(num_words)
