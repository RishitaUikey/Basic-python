'''Write a  Python program to verify that all values in a dictionary are the same.
Original Dictionary:
{'Cierra Vega': 12, 'Alden Cantrell': 12, 'Kierra Gentry': 12, 'Pierre Cox': 12}
Check all are 12 in the dictionary.
True
Check all are 10 in the dictionary.'''

student_scores = {
    'Cierra Vega': 12,
    'Alden Cantrell': 12,
    'Kierra Gentry': 12,
    'Pierre Cox': 12
}

all_same = len(set(student_scores.values())) == 1
print("Check all are 12 in the dictionary.")
print(all_same)

print("Check all are 10 in the dictionary.")
print(len(set(student_scores.values())) == 1 and list(set(student_scores.values()))[0] == 10)
