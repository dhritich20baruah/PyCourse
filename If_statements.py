cars = ['maruti', 'mahindra', 'tata', 'vw']

for car in cars:
    if car == 'vw':
        print(car.upper())
    else:
        print(car.title())

car = 'bmw'
auto = 'Bmw'
print(car == auto) #False equality check is case sensitive
#Test for inequality
requested_topping = 'mushrooms'
if requested_topping != 'anchovies':
    print("Hold the anchovies")

ans = 23
if ans != 34:
    print('not equal')

#Check multiple conditions: when both the conditions should satisfy
age_1 = 22
age_2 = 18
x = age_1 >= 21 and age_2 >= 21
print(x)

#or: either of the conditions satisfy
age_3 = 22
age_4 = 18
x = age_3 >= 21 or age_4 >= 21
print(x)

#Check whether a value is in a list
requested_toppings = ['mushroom', 'onion', 'pineapple']
print('mushroom' in requested_toppings)
print('pepperoni' in requested_toppings)

#Check whether a value is not in the list
users = ['andy', "matt", "tom"]
user = "tim"

if user not in users:
    print(f"{user.title()}, you can post a response.")

#if statements
age = 19
if age>=18:
    print("You are old enough to vote.")

#if-else statement
age = 17
if age>=18:
    print("You are old enough to vote.")
else:
    print("Sorry! you are too young to vote.")

#if-elif-else statement
price = 1000
if price<200:
    print("Discount is 5%")
elif price<500:
    print("Discount is 10%")
else:
    print("Discount is 15%")

#Multiple elif blocks
price = 750
if price<200:
    Discount = 5
elif price<500:
    Discount = 10
elif price<800:
    Discount = 12
else:
    Discount = 15 #The else block can be ommited can sometimes include malicious or invalid data becoz no other conditions are met it will always be executed
print(f"The discount offered is {Discount}%")

#testing multiple conditions
requested_toppings = ['mushroom', 'onion', 'pineapple']
if 'mushroom' in requested_toppings:
    print("Adding mushroom")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni")
if 'onion' in requested_toppings:
    print('Adding onion')