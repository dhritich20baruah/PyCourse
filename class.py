# Class Dog is declared and class name should be capitalized
class Dog: 
    """A simple attempt to model a dog"""
# A function that is a part of a class is called a method
# The __init__() method is a special method that Python runs automatically when ever we create a new instance based on a class.
    def __init__( self, name, age):
        """Initialize name and age attrinutes"""
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