import random
import hangman_art
from hangman_art import stages

words = ["goal", "determination", "dedication"]
lives = 6
# random.choice() : it randomly picks an element from the given list
word = random.choice(words)
# firstly making a list of the size of word chosen and filling it with '_'
guess = list(len(word) * '_')
# The loop will goes until the hangman completely lost his lives or the word been correctly guessed i.e
# there were no blankds

print(hangman_art.logo)
while "_" in guess:
    char = input("Enter your guess letter: ")
    if char in word and (char not in guess):
        for j in range(0, len(word)):
            if word[j] == char:
                guess[j] = char
                print("".join(guess))
            if "_" not in guess:
                print("You Saved my Life")
    else:
        print("You have entered the wrong letter")
        print(stages[lives])
        lives -= 1
        if lives == -1:
            print("You Lost")
            break
