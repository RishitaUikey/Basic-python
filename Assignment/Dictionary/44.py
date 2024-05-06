'''Write a  Python program to filter the height and width of students, which are stored in a dictionary.
Original Dictionary:
{'Cierra Vega': (6.2, 70), 'Alden Cantrell': (5.9, 65), 'Kierra Gentry': (6.0, 68), 'Pierre Cox': (5.8, 66)}
Height > 6ft and Weight> 70kg:
{'Cierra Vega': (6.2, 70)}'''

students = {
    'Cierra Vega': (6.2, 70),
    'Alden Cantrell': (5.9, 65),
    'Kierra Gentry': (6.0, 68),
    'Pierre Cox': (5.8, 66)
}

filtered_students = {name: (height, weight) for name, (height, weight) in students.items() if height > 6 and weight > 70}
print("Height > 6ft and Weight > 70kg:")
print(filtered_students)
