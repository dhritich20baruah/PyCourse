def greet_user(username):
    """Display a simple greeting"""
    print(f"Hello, {username.title()}!")

greet_user('Delta')

#passing arguments
def describe_pet(animal_type, pet_name):
    """Display information about a pet"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")
    print(f"His/her name is {pet_name.title()}.")

describe_pet('hamster', 'Harry')
describe_pet('dog', "Lali")# Multiple function calls
describe_pet(animal_type='cat', pet_name='Rupsi')
#Key word arguments

def describe_pet(animal_type, pet_name):
    """Display information about a pet"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet(animal_type="hamster", pet_name='harry')

# DEfault values
def describe_pet(pet_name, animal_type="dog"):
    """Display information about a pet"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet(pet_name='Jerry')

# Equivalent function calls
#A dog named Willie
describe_pet('Willie')
describe_pet(pet_name='Tommy')
#A hamster named Harry
describe_pet('Harry', 'hamster')
describe_pet(pet_name="Harry", animal_type='hamster')




