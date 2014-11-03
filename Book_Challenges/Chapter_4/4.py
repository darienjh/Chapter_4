import random

words = ("school", "book", "work", "highschool", "linux", "Command", "Jumble")

word = random.choice(words)

tries = 0

correct = word

jumble = ""
while word:
    position = random.randrange(len(word))
    jumble += word[position]
    word = word[:position] + word[(position + 1):]

print(" Welcome to guess the word")

print("The word is:", jumble)

guess = input("Your guess: ")
while guess != correct and guess != "":
    print("The word has",len(correct))
    while tries != 5:
        print("you have" +1)

if guess == correct:
    print("Correct! We haave a winner!!!!")

input("Please press enter to exit")


    
