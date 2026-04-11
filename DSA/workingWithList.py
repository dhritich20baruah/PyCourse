tata = ['altroz', 'tiago', 'tigor', 'safari', 'harrier']
for cars in tata:
    # print(cars)
    print(f"{cars.title()} is a great car.")
    print(f"Cann't wait for the next generation of {cars.title()}.\n")

# Range function
for value in range(1,5):
    print(value)#doesnot print number 5
for value in range(6):
    print(value)#will print from 0 to 5
# use range to make a list of numbers
numbers = list(range(1,6))
print(numbers)
even_numbers = list(range(2,11,2))
print(even_numbers)
# print square of first 10 numbers
squares = []
for value in range(1,11):
    square = value**2
    squares.append(square)
print(squares)
print(min(squares))
print(max(squares))
print(sum(squares))
# List Comprehension
sq = [value**2 for value in range(1,11)]
print(sq)
#slicing a list
names = ["alpha", "bravo", "charlie", "delta", "echo"]
print(names[0:3])#the code prints the slice of the list of first three names starting with index 0 and ends at index 2
print(names[1:4]) #starts at 1 ends at 3
print(names[:3])# automatically starts at 0
print(names[2:])# returns all items from third to the end
print(names[-3:])# returns the last three items
#Looping through a slice
print('Here are the first three names from the list')
for name in names[:3]:
    print(name.title())

#Copying a list
food = ["Rice", "potato", "fish", "chicken", "egg"]
fav_food= food[:]
print(fav_food)
fav_food.append("roti")
food.append("apple")
print(food)
food = fav_food #this won't work both variables will simply point to the same list
print(food)