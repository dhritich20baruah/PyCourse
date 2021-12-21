alien_0 = {'color': 'green', 'points': 5}

print(alien_0['color'])
print(alien_0['points'])

new_points = alien_0['points']
print(f"You just earned {new_points}")

alien_0['x_position'] = 0
alien_0['y_position'] = 25

#Empty dictionary
alien_0 = {}
alien_0['color'] = 'green'
alien_0['points'] = 5

print(alien_0)
# Modifying values
alien_0 = {'color': 'red'}
print(f"The alien is of {alien_0['color']} color.")

alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f"Original position: {alien_0['x_position']}")
#Move the alien to the right
#Determine how far to move the alien based on its current speed.
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    #This must be a fast alien
    x_increment = 3
#The new position is the old position plus the increment.
alien_0['x_position'] = alien_0['x_position'] + x_increment

print(f"New position: {alien_0['x_position']}")

# Removing key value pairs
del alien_0['speed']
print(alien_0)

# A dictionary of similiar objects
favorite_language = {
    'jen': 'python',
    'sarah': 'C',
    'edward': 'ruby',
    'phil': 'python',
}

language = favorite_language['sarah'].title()
print(f"Sarah's favorite language is {language}.")

# get() method first argument what you are trying to retrieve second value is fallback if the key doesnot exist
point_value = alien_0.get('points', 'No point value assigned')
print(point_value)

# Looping through all key value pairs
user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi'
}
for key, value in user_0.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")

for name, language in favorite_language.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")

# Looping through all the keys in a Dictionary
for name in favorite_language.keys():
    print(name.title())
# The following code has the same output looping through keys is the default behaviour
for name in favorite_language:
    print(name.title())

friends = ['phil', 'sarah']
for name in favorite_language.keys():
    print(name.title())

    if name in friends:
        language = favorite_language[name].title()
        print(f"\t{name.title()}, I see you love {language}!")

if 'erin' not in favorite_language.keys():
    print("Erin, please take our poll!")

#Looping through a dictionary's keys in a particular order
for name in sorted(favorite_language.keys()):
    print(f"{name.title()}, thank you for taking the poll.")

#Looping through all the values in a dictionary
print('The following languages have been mentioned:')
for language in favorite_language.values():
    print(language.title())

#To loop through a large collection with repeated values use set
print("The following languages have been mentioned")
for language in set(favorite_language.values()):
    print(language.title())

# Nested dictionary
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}
aliens = [alien_0, alien_1, alien_2]
for alien in aliens: 
    print(alien)

#Make an empty list for storing aliens
aliens = []
#Make 30 green aliens
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

#Show the first 5 aliens
for alien in aliens[:5]:
    print(alien)
print('...')

#Show how many aliens have been created
print(f"Total number of aliens: {len(aliens)}")

for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10

for alien in aliens[:5]:
    print(alien)
print('...')

pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese']
}
print(f"You ordered a {pizza['crust']}-crust pizza"
    "with the following toppings:")

for topping in pizza['toppings']:
    print('\t' + topping)

favorite_language = {
    'jen': ['python', 'ruby'],
    'sarah': ['C'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell']
}

for name, languages in favorite_language.items():
    print(f"\n{name.title()}'s favorite languages are:")
    for language in languages:
        print(f"\t{language.title()}")

# A Dictionary in a Dictionary 
users = {
    'aeinstein':{
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton'
    },
    'mcurie':{
        'first': 'marie',
        'last': 'curie',
        'location': 'Paris',
    },
}

for username, user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_info['first']}{user_info['last']}"
    location =user_info['location']
    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")