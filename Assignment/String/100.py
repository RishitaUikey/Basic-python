'''Write a  Python program to check whether any word in a given string contains duplicate characters or not. Return True or False.
Sample Output:
Original text:
Filter out the factorials of the said list.
Check whether any word in the said sting contains duplicate characrters or not!
False
Original text:
 Python Exercise.
Check whether any word in the said sting contains duplicate characrters or not!
False
Original text:
The wait is over.
Check whether any word in the said sting contains duplicate characrters or not!
True'''
def has_duplicate_characters(word):

    seen = set()
    for char in word:
        if char in seen:
            return True
        seen.add(char)
    return False

def contains_word_with_duplicates(input_str):
    words = input_str.split()
    for word in words:
        if has_duplicate_characters(word):
            return True
    return False
def main():
    texts = [
        "Filter out the factorials of the said list.",
        "Python Exercise.",
        "The wait is over."
    ]
    for text in texts:
        print("Original text:")
        print(text)
        print("Check whether any word in the said string contains duplicate characters or not!")
        print(contains_word_with_duplicates(text))

if __name__ == "__main__":
    main()
