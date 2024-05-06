'''Write a  Python program to insert space before every capital letter appears in a given word.
Sample Data:
("PythonExercises") -> "Python Exercises"
("Python") -> "Python"
("PythonExercisesPracticeSolution") -> "Python Exercises Practice Solution"'''

def insert_space_before_capital(word):
    result = ''
    
    for char in word:
        if char.isupper() and result:
            result += ' ' + char
        else:
            result += char
    
    return result

samples = [
    "PythonExercises",
    "Python",
    "PythonExercisesPracticeSolution"
]
for sample in samples:
    print(f'("{sample}") -> "{insert_space_before_capital(sample)}"')
