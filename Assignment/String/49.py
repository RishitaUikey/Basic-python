'''Write a Python program to count and display vowels in text.'''

def count_and_display_vowels(text):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    vowel_count = 0
    displayed_vowels = ""
    for char in text:
        if char.lower() in vowels:
            vowel_count += 1
            displayed_vowels += char + ' '
    print("Number of vowels:", vowel_count)
    print("Vowels:", displayed_vowels)
text = "Hello World! This is a test text."
count_and_display_vowels(text)
