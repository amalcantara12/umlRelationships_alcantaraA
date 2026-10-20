#inheritance

class Animal:
    def __init__(self, name, breed, color):
            self.name = name
            self.breed = breed
            self.color = color

class Dog(Animal):
    def bark(self):
        print(self.name, "is barking!")

doggie = Dog("Cole", "Black Retriever", "Black")
doggie.bark()
