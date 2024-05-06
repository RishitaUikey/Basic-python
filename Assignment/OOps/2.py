# Write a Python program to create a person class. Include attributes like name, country and date 
# of birth. Implement a method to determine the person's age.

from datetime import datetime

class Person:
    def __init__(self, name, country, dob):
        self.name = name
        self.country = country
        self.dob = datetime.strptime(dob, "%Y-%m-%d").date()

    def calculate_age(self):
        today = datetime.now().date()
        age = today.year - self.dob.year - ((today.month, today.day) < (self.dob.month, self.dob.day))
        return age

# Example usage:
name = input("Enter name: ")
country = input("Enter country: ")
dob = input("Enter date of birth (YYYY-MM-DD): ")

person = Person(name, country, dob)
age = person.calculate_age()
print(f"{person.name} is {age} years old.")
