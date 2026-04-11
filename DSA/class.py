# Class Dog is declared and class name should be capitalized
class Dog: 
    """A simple attempt to model a dog"""
# A function that is a part of a class is called a method
# The __init__() method is a special method that Python runs automatically when ever we create a new instance based on a class.
    def __init__( self, name, age):
        """Initialize name and age attributes"""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting in response to a command"""
        print(f"{self.name} is now sitting")

    def roll_over(self):
        print(f"{self.name} roll over")

my_dog = Dog('Willie', 6)

print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old")

your_dog = Dog('Lucy', 3)
print(f"My dog's name is {your_dog.name}.")
print(f"My dog is {your_dog.age} years old")
your_dog.sit()

# WORKING WITH CLASSES AND INSTANCES
class Car:
    """A simple attempt to represent a car"""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0 #Setting a default value for attribute

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year}{self.make}{self.model}"
        return long_name.title()

    def read_odometer(self):
        print(f"This cas has {self.odometer_reading} miles on it")   

my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()