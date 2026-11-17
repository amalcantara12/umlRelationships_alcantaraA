class Person:
    def __init__ (self, name, age):
        self.__name = name
        self.__age = age

    def getName (self):
        print("Name: ", self.__name)

    def getAge (self):
        print("Age: ", self.__age)

    def display_info(self):
        self.getName()
        self.getAge()

person1 = Person("Arya", 14)
person1.display_info()