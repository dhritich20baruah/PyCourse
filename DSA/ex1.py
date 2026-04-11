Dictionary = {
    "clock": "device that gives time",
    "linked": "connected",
    "mask": "covering a thing",
    "switch": "change",
    "perfume": "substance that smells good"
}

# word = input("Tell me what do you want to know about: ")

# print(Dictionary[word])

expences = {"January": 2200,
"February": 2350,
"March":2600,
"April":2130,
"May":2190}

x = expences["February"]-expences["January"]
print(x)

y = expences["February"]+expences["January"]+expences["March"]
print(y)

for z in expences.values():
    if z==2000:
        print("yes")
    else:
        print("no")

expences["June"] = 1980
print(expences)
expences["April"] = expences["April"] - 200
print(expences)

heros=['spider man','thor','hulk','iron man','captain america']
print(len(heros))
heros.append("black panther")
print(heros)
heros.remove("black panther")
heros.insert(3, "black panther")
heros[1:3]=["Dr. Strange"]
heros.sort(key = str.lower)
print(heros)

numList = []
maxNum = input("Give a maximum number: ")
z = int(maxNum)
for x in range(0, z):
    if x%2 != 0:
        numList.append(x)

print(numList)