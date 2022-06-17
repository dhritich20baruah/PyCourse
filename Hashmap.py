stock_prices = []
with open("stock_prices.csv","r") as f:
    for line in f:
        tokens = line.split(',')
        day = tokens[0]
        price = float(tokens[1])
        stock_prices.append([day,price])
    
print(stock_prices)

print(stock_prices[0])

# Find stock price on March9
for element in stock_prices:
    if element[0] == '9-Mar':
        print(element[1])

# Complexity of search using a list is O(n)

# Process using python dictionary
stock_prices = {}
with open("stock_prices.csv", "r") as f:
    for line in f:
        tokens = line.split(',')
        day = tokens[0]
        price = float(tokens[1])
        stock_prices[day] = price

print(stock_prices)

# Find stock price on March 9:
print(stock_prices["9-Mar"])

# Complexity of search using a dictionary is O(n)

# Implement Hash Table
def get_hash(key):
    hash = 0
    for char in key:
        hash += ord(char) #ord() finds ASCII character
    return hash % 100

print(get_hash('6-Mar'))

class HashTable:
    def __init__(self):
        self.MAX = 100 #setting the size of the array using list comprehension
        self.arr = [None for i in range(self.MAX)]
    
    def get_hash(self, key):
        hash = 0
        for char in key:
            hash += ord(char)
        return hash % self.MAX

    def __getitem__(self, index):
        h = self.get_hash(index)
        return self.arr[h]
    
    def __setitem__(self, key, val):
        h = self.get_hash(key)
        self.arr[h] = val
    
    def __delitem__(self, key):
        h = self.get_hash(key)
        self.arr[h] = None

t = HashTable() #create an object of class
t['14-Mar'] = 130
t['16-Mar'] = 250
t['18-Mar'] = 300
del t['16-Mar']
print(t['14-Mar'])

# Hash table collision handling using chaining

class HashTable:
    def __init__(self):
        self.MAX = 10
        self.arr = [[] for i range(self.MAX)]

    def get_hash(self, key):
        hash = 0
        for char in key:
            hash += ord(char)
        return hash % self.MAX
    
    def __getitem__(self, key):
        arr_index = self.get_hash(key)
        for kv in self.arr[arr_index]:
            if kv[0] == key:
                return kv[1]
    
    def __setitem__(self, key, val):
        h = self.get_hash(key)
        found = False
        for idx, element in enumerate(self.arr[h]):
            if len(element) == 2 and element[0] == key:
                self.arr[h][idx] = (key, val)
                found = Trus
        if not found :
            self.arr[h].append((key, val))

    def __delitem__(self, key):
        arr_index = self.get_hash(key)
        for index, kv in enumerate(self.arr[arr_index]):
            if kv[0] == key:
                print("del", index)
                del self.arr[arr_index][index]