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
        hash += ord(char)
    return hash % 100

print(get_hash('6-Mar'))

class HashTable:
    def __init__(self):
        self.Max = 100
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

t = HashTable()
t["6-Mar"] = 310
t["7-Mar"] = 410

print(t.arr)