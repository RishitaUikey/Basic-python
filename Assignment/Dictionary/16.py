# Write a  Python program to get a dictionary from an object's fields.

class Person:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

person = Person("Alice", 30, "New York")
person_dict = vars(person)
print(person_dict)
