def hangman_game():

    import time

    print(" ------------------------------------------------") 
    print("|                                                |")
    print("|                                                |")
    print("|    Welcome to a game of Hangman!!!             |")
    print("|                                                |")
    print("|                                                |")
    print(" ------------------------------------------------")

    import random

    name = input("What is your name? ")

    print("")
    print("Hello", name, "and I hope you are ready for a game of hangman!!")

    words = ['cheese', 'monke', 'Poopyfarts', 'nuts',
            'cutlery', 'beach', 'examine', 'suffering',
            'sensei', 'logic', 'bubbles', 'cornflour', 
            'determined', 'mitochondria', 'academia', 
            'titans', 'hangman', 'emergency' ]

    word = random.choice(words)

    x = len(word)

    time.sleep(1)

    print("")
    print("")
    print("There are", x, "characters in the word")

    time.sleep(1)

    print("")
    print("Guess the characters: ")

    guesses = ""
    turns = 20

    while turns > 0:
        failed = 0

        for char in word:
            if char in guesses:
                print(char)
            else:
                print("_")
                failed += 1
        
        if failed == 0:
            print("")
            print("Congratulations", name, "you are the champion!!")
            print("")
            print("The word was: ", word)
            print("")
            break

        guess = input("guess a character:")
        guesses += guess

        if guess not in word:
            turns -= 1
            print("")
            print("Not correct, try again.")
            print('')
            print("You have", + turns, 'more guesses')

            if turns == 0:
                print("")
                print("Oh no!!", name, "You Lose")
                break
                
hangman_game()
