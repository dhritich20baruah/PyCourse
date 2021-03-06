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

# Return values
def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted"""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)

# Make arguments optional
def get_formatted_name(first_name, last_name,middle_name=''):
    """Return a full name, neatly formatted"""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
musician = get_formatted_name('Sir', 'Elvis', 'Presly')
print(musician)

# Returning a Dictionary
def build_person(first_name, last_name):
    """Return a dictonary of information about a person"""
    person = {'first': first_name, 'last': last_name}
    return person

musician = build_person('jimi', 'hendrix')
print(musician)

def build_person(first_name, last_name, age=None):
    """Return a dictonary of information about a person"""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person

musician = build_person('jimi', 'hendrix', age=30)
print(musician)

# Using a function with a while loop
def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted"""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

while True:
    print('\nPlease tell me your name:')
    print("(enter 'q' at any time to quit)")

    f_name = input("First name: ")
    if f_name == 'q':
        break
    l_name = input("Last name: ")
    if l_name == 'q':
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello, {formatted_name}")

# Modifying a list in a function
#Start with some designs that need to be printed
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

#simulate printing each design, until none are left
#Move each design to completed_models after printing
while unprinted_designs:
    current_design = unprinted_designs.pop()
    print(f"Printing model: {current_design}")
    completed_models.append(current_design)

#Display all completed models.
print("\nThe following models have been printed:")
for completed_model in completed_models:
    print(completed_model)

# the above code is being written with two function
def print_models(unprinted_designs, completed_models):
    """
    Simulate printing each design, until none are left.
    Move each design to completed_models after printing.
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """Show all the models that were printed."""
    print('\nThe following models have been printed')
    for completed_model in completed_models:
        print(completed_model)

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)

# Preventing a function from modifying a list
# Pass a copy of the list not the original
# function_name(list_name[:])
print_models(unprinted_designs[:], completed_models)

# Passing an arbitrary number of arguments
def make_pizza(*toppings):
    """Print the list of toppings that has been requested"""
    print(toppings)
    for topping in toppings:
        print(f"{topping}")

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

# *toppings tells python to make an empty tupple called toppings and pack in all the value ot recieves

# Mixing Positional and arbitrary arguments
def make_pizza(size, *toppings):
    """Print the list of toppings that has been requested"""
    print(f"\nMaking a {size}-inch pizza with the following toppings")
    for topping in toppings:
        print(f"{topping}")
# Size is positonal argument and arbitrary arguments must be placed lastq
make_pizza(16,'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
# Using arbitrary keyword arguments
def build_profile(first, last, **user_info):
    """Build a distionary containing everything we know a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('albert', 'einstein', location='princeton', field='physics')

print(user_profile)
# The parameter **user_info cause Python to create an empty dictionary called user_info and pack whatever name-value pairs it receives into this dictionary

# Storing your functions in modules
def make_pizza(size, *toppings):
    """Print the list of toppings that has been requested"""
    print(f"\nMaking a {size}-inch pizza with the following toppings")
    for topping in toppings:
        print(f"{topping}")

# In the same directory create a hypothetical separate file called making_pizza.py then import the module and then make two calls to make_pizza()
import pizza

pizza.make_pizza(16, 'pepperoni')
pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# module_name.function_name()