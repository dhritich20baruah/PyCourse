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