print(" ------------------------------------------------") 
print("|                                                |")
print("|                                                |")
print("|    Welcome to a game of Hangman!!!             |")
print("|                                                |")
print("|                                                |")
print(" ------------------------------------------------")

print("")
print("Please enter your names")

player1 = input("Player 1 is... ")
player2 = input("Player 2 is... ")
print("")
print("Ok now.... it is", player2, "'s turn to guess.", player1, "please hide the screen")
print("")

print(player1, "please type the word that you want", player2, "to guess:")
word = input()
print("The word you have chosen is...")
print(word)

start = input("Type 'yes' to continue the game or type 'no' to re-enter the word: ")

if start == "yes":
    print("we get it")
elif start == "no":
    word = input("Please type your chosen word: ")
    print(word)
else:
    print("Try Again")
    print("")
    input("Type 'yes' to continue the game or type 'no' to re-enter the word")




