# How input() function works

# message = input('Tell me something, and i will repeat it back to you: ')
# print(message)

# //////////////////
# Multi line prompt
# prompt = "If you tell us who you are, we can personalize the message you see"
# prompt += "\nWhat is your name?"

# name = input(prompt)
# print(f"\nHello, {name}!")

# Using int() to Accept Numerical Input
# age = input("How old are you?")
# print(age)
# # Input is converted into a string by python
# # If we try to use the input as number it will be responded with error
# # Convert it to integer by int(age)
# age = int(age)
# print(age >= 18)

# height = input("How tall are you, in inches?")
# height = int(height)
# if height>=48:
#     print('\nYou are tall enough to ride!')
# else:
#     print('\nYou are not tall enough')

# The Modulo Operator
# number = input("Enter a number, and I'll tell you if it's even or odd: ")
# number = int(number)

# if number % 2 == 0:
#     print(f"\nThe number {number} is even")
# else:
#     print(f"\nThe Number {number} is odd")


# While Loop
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1

# Letting the User choose when to quit
# prompt = "\nTell me something, and I will repeat it back to you: "
# prompt += "\nEnter 'quit' to end the program."
# message = ""
# while message != 'quit':
#     message = input(prompt)

#     if message != 'quit':
#         print(message)

#################
# Flag
# prompt = "\nTell me something, and I will repeat it back to you: "
# prompt += "\nEnter 'quit' to end the program."
# active = True
# while active:
#     message = input(prompt)

#     if message == 'quit':
#         active = False
#     else:
#         print(message)

###############
#Using break to exit a loop
# prompt = "\nPlease enter the name of a city you have visited: "
# prompt += "\n(Enter 'quit' when you are finished.)"
# while True: 
#     city = input(prompt)
#     if city == 'quit':
#         break
#     else:
#         print(f"I'd love to go to {city.title()}")

######################
#Using continue in a loop
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)

# Using a while loop with list and dictionaries
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []
while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user)

print('\nThe following users have been confirmed:')
for confirmed_user in confirmed_users:
    print(confirmed_user.title())

# Remove all instances of a specific values from a list
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')

print(pets)

# Filling a Dictionary with User Input
responses = {}
#set a flas to indicate that apolling is active
polling_active = True
while polling_active:
    name = input("\nWhat is your name?")
    response = input("What will you study today?")
    # Store the responses in the dictionary.
    responses[name] = response
    # Find out if anyone else is going to take the poll
    repeat = input("Would you like to let another person repond? (yes/no)")
    if repeat == 'no':
        polling_active = False

# Polling is complete. Show the results.
print("\n---Poll Results---")
for name, response in responses.items():
    print(f"{name} would like to study {response}.")
