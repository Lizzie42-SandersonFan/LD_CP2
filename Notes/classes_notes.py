# LD 1st Classes Notes

# Example 1
class Animal:
    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age

    def __str__(self):
        return f"Name: {self.name}\nSpecies: {self.species}\nAge: {self.age}\n"
    
    def birthday(self):
        self.age += 1

dog = Animal("Doug", "Dog", 4)
bunny = Animal("Judy", "Rabbit", 20)
elephant = Animal("George", "African Elephant", 50)

print(dog)
print(bunny)
print(elephant)
dog.birthday()
print(dog)

# Example 2
class ClassPeriod:
    def __init__(self, subject, teacher = "Ms. LaRose", room = None):
        self.subject = subject.title()
        self.teacher = teacher.title()
        self.room = room

    def __str__(self):
        return f"Subject: {self.subject}\nTeacher: {self.teacher}\nRoom: {self.room}\n"
    