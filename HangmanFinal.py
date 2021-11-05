def starter():
    print(" ------------------------------------------------") 
    print("|                                                |")
    print("|                                                |")
    print("|    Welcome to a game of Hangman!!!             |")
    print("|                                                |")
    print("|                                                |")
    print(" ------------------------------------------------")

starter()

print("")
print("Please enter your names")

player1 = input("Player 1 is... ")
player2 = input("Player 2 is... ")

print("")
print("")
print("Ok now.... it is", player2, "'s turn to guess.", player1, "please hide the screen")
print("")

print(player1, "please type the word that you want", player2, "to guess:")
word = input()
print("The word you have chosen is...")
print(word)

start = input("Type 'yes' to continue the game or type 'no' to re-enter the word: ")

yes = "yes"

if start != "yes":
    word = input("Please type your chosen word: ")
    print("Your new word is:", word)
    input("Press enter to begin the game")
    import os
    os.system('cls')
else:
    input("Press enter to begin the game")
    import os
    os.system('cls')

import time
time.sleep(1)

print("")
print("Ok now....it is time for", player1, "to guess the word")
print("")
print("")

x = len(word)

print ("There are", x, "characters in the word:")

guesses = ""

turns = "15"

while turns != 0:
    failed = 0

    for guess in word:
        if guess in guesses:
            print(guess)
        else:
            print("_")
    if failed == 0:
        print(player1, "is the winner!!")
        print("The word is:", word)
        break

guess = input("Guess a character: ")
    
guesses += guess

if guess not in word:
    turns -= 1
    print("Wrong")
    print("You have", + turns, 'more guesses')

    if turns == 0:
        print(player1, "loses", player2, "wins!!!")
