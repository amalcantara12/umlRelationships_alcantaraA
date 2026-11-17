class Person:
    def __init__ (self, name, age):
        self.name = name
        self.__age = age

    def getAge (self):
        print("Age: ", self.__age)

    def display_info(self):
        self.getAge()

person1 = Person("Nina", 20)
print("Name: ", person1.name)
person1.display_info()