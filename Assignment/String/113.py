'''Write a  Python program that returns a string sorted alphabetically by the first character of a given string of words.
Sample Data:
("Red Green Black White Pink") -> "Black Green Pink Red White"
("Calculate the sum of two said numbers given as strings.") -> ("Calculate as given numbers of sum said strings. the two")
("The quick brown fox jumps over the lazy dog.") -> ("The brown dog. fox jumps lazy over quick the")'''

def sort_words_alphabetically_by_first_character(text):
    words = text.split()
    sorted_words = sorted(words, key=lambda x: x[0].lower())
    return ' '.join(sorted_words)
samples = [
    "Red Green Black White Pink",
    "Calculate the sum of two said numbers given as strings.",
    "The quick brown fox jumps over the lazy dog."
]
for sample in samples:
    print(f'("{sample}") -> "{sort_words_alphabetically_by_first_character(sample)}"')
