words = {
    'clock': 'device that gives time',
    'linked': 'connected',
    'mask': 'covering a thing',
    'switch': 'change',
    'perfume': 'substance that smells good'
}

message = input("Tell me what do you want to know about: ")

prompt = input(message)

print(words[message])

# for word, meaning in words:
#     if prompt == word:
#         print(meaning)