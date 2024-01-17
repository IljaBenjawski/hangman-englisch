import random

print('Welcome to Hangman')

word_list = ('apply', 'me', 'please', 'for', 'this', 'job', 'hangman')

word = random.choice(word_list)
letters = []
display_word = ['_'] * len(word) # display word ist so groß wie die länge (len) des wortes

user_try = 0
max_attempts = 5

while user_try < max_attempts:
    user_guess = input('\nGuess a Letter: ').lower()

    if len(user_guess) != 1 or not user_guess.isalpha():
        print("Please enter a single letter.")
        continue

    if user_guess in letters:
        print("You've already guessed that letter.")
        continue

    letters.append(user_guess)

    if user_guess in word:
        for i in range(len(word)): # so goß wie das wort, Position wird überprüft
            if word[i] == user_guess: # Wenn der Buchstabe in der aktuellen Position mit dem geratenen Buchstaben übereinstimmt:

                display_word[i] = user_guess   # Aktualisiere das display_word an dieser Position mit dem geratenen Buchstaben.

    else:
        user_try += 1

    print(' '.join(display_word))# Gebe das aktualisierte display_word aus. Hier werden geratene Buchstaben und Unterstriche angezeigt.

    if ''.join(display_word) == word:
        print("Congratulations! You've guessed the word:", word)
        break

if user_try == max_attempts:
    print("Sorry, you've run out of attempts. The word was:", word)
