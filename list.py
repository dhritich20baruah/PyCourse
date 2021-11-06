birds = ["owl", "eagle", "parrot", "shrike"]
print(birds)
print(birds[0])
print(birds[0].title())
print(birds[-1])
message = f"The {birds[1].title()} has landed." # f string with list
print(message)
print(birds)
birds[2] = "sparrow" #Replacing the element in index 2
birds.append("parrot") # Append a new item to the list
# elements can be appended to an entirely empty list
birds.insert(1, 'oriole')#Insert a new element in a list //list.insert(index, 'new element)
print(birds) 
del birds[3] #remove element by the index number
popped_birds = birds.pop() #removes the last item from the list and stores it
print(popped_birds); 
#Remove an item by value
removed_birds = 'oriole'
birds.remove(removed_birds)
print(f"Remove two birds {removed_birds} and {popped_birds} ")
birds.sort() # the sort method sorts the list alphabetically and permanently
birds.sort(reverse=True)
print(birds)
birds.append("Duck")
birds.append("Kingfisher")
print(sorted(birds)) # sorts the list temporarily
birds.reverse()
print(birds)
print(len(birds))
