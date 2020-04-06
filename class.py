# class = function + variable
# object = output with use class

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def say_hello(self, to_name):
        print("Hi! " + to_name +  " I am " + self.name)

    def introduce(self):
        print("My name is " + self.name + " and I am " + str(self.age) + " old")

class Police(Person):
    def arrest(self, to_arrest):
        print("You are under arrest, " + to_arrest)

class Programmer(Person):
    def program(self, to_program):
        print("What should i make next? Ah, I will make this one" + to_program)

Chanyoung = Person("chan" , 33)
Jenny = Police("Jenn", 24)
Michael = Programmer("Mic", 29)

# Chanyoung.arrest("Jenn")
Jenny.introduce()
Jenny.arrest("chan")
Michael.introduce()
Michael.program("Email client")

# Chanyoung = Person("Chanyoung", 33)
# James = Person("James", 34)
# Jenny = Person("Jenny", 24)

# Chanyoung.say_hello("Cheol")
# James.say_hello("Yeong")
# Jenny.say_hello("Mijee")

# Chanyoung.introduce()