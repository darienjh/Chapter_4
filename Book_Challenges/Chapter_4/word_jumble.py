# Word Jumble
#
# The computer picks a random word and then "jumbles" it
# The player has to guess the original word

import random

# create a sequence of words to choose from
WORDS = ("python", "jumble", "easy", "difficult", "answer", "xylophone")
# pick one word randomly from the sequence
word = random.choice(WORDS)
# create a variable to use later to see if the guess is correct
correct = word
points = 100
# create a jumbled version of the word
jumble =""
while word:
    position = random.randrange(len(word))
    jumble += word[position]
    word = word[:position] + word[(position + 1):]

# start the game
print(
"""
           Welcome to Word Jumble!
        
   Unscramble the letters to make a word.
(Press the enter key at the prompt to quit.)
"""
)
print("The jumble is:", jumble)

guess = input("\nYour guess: ")
while guess != correct and guess != "":
    print("Sorry, that's not it.")
    hint = input("Would you like a hint?")
    if correct == "python":
        print("It slithers")
    elif correct == "jumble":
        print("another term for mixing")
    elif correct == "easy":
        print("If you understand it is ...")
    elif correct == "difficult":
        print("if you DONT understand it is...")
    elif correct == "answer":
        print("do you know the a.....??")
    elif correct == "xylophone":
        print("what instrument starts with X?")
    guess = input("Your guess: ")
    print("you won", points-10 ,"points")

if guess == correct:
    print("That's it!  You guessed it!\n")
    print("You won", points, "points")

print("Thanks for playing.")

input("\n\nPress the enter key to exit.")
