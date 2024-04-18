'''Write a Python program that accepts the number of subjects, subject names and marks. Input the number of subjects and then the subject name and marks separated by a space on the next line. Print the subject name and marks in order of appearance.
Sample Output:
Powered by
Number of subjects: 3
Input Subject name and marks: Bengali 58
Input Subject name and marks: English 62
Input Subject name and marks: Math 68
Bengali 58
English 62
Math 68'''

def input_subjects(num_subjects):
    subjects = []

    for i in range(num_subjects):
        subject, marks = input("Input Subject name and marks: ").split()
        subjects.append((subject, marks))

    for subject, marks in subjects:
        print(subject, marks)

print("Powered by")
num_subjects = int(input("Number of subjects: "))
input_subjects(num_subjects)
