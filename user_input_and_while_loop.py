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
number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)

if number % 2 == 0:
    print(f"\nThe number {number} is even")
else:
    print(f"\nThe Number {number} is odd")
