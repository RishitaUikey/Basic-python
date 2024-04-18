'''Write a Python program to find the second lowest total marks of any student(s) from the given names and marks of each student using lists and lambda. Input number of students, names and grades of each student.
Sample Output:
Input number of students: 3
Name: Avik Das
Total marks: 89
Name: ayan Roy
Total marks: 75
Name: Sayan Dutta
Total marks: 93
Names and Marks of all students:
[['Avik Das ', 89.0], ['ayan Roy', 75.0], ['Sayan Dutta', 93.0]]
Second lowest Marks: 89.0
Names:
Avik Das'''

num_students = int(input("Input number of students: "))
students = []

for _ in range(num_students):
    name = input("Name: ")
    marks = float(input("Total marks: "))
    students.append([name, marks])

students.sort(key=lambda x: x[1])

second_lowest_marks = sorted(set(marks for name, marks in students))[1]
names_second_lowest_marks = [name for name, marks in students if marks == second_lowest_marks]

print("Names and Marks of all students:")
print(students)

print("Second lowest Marks:", second_lowest_marks)

print("Names:")
for name in names_second_lowest_marks:
    print(name)
