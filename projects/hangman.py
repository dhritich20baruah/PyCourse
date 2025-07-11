import random
from words import words
import string

def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word

def hangman():
    word = get_valid_word(words)
    word_letters = set(word) #letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set() #what the user has guessed

    # getting user input
    while len(word_letters) >0:
        # letters used
        # ' '.join(['a', 'b', 'cd']) ---> 'a b cd'
        print('You have used these letters: ', ' '.join(used_letters))

        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))

        used_letter = input('Guess a letter: ').upper()
        if used_letter in alphabet - used_letters:
            used_letters.add(used_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)

        elif user_letter in used_letters:
            print('You have already used that character.please try again')

        else: 
            print('Invalid character. Please try again.')

user_input = input('Type something: ')
print(user_input)
 