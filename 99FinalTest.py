# Assigns a function to the whole menu
def my_menu():

    print(" ------------------------------------------------") 
    print("|                                                |")
    print("|    O7Menu                                      |")
    print("|    Name : Nikhita Arora                        |")
    print("|    Version : 01                                |")
    print("|                                                |")
    print(" ------------------------------------------------")
    print("")

    # List
    print("1. Hello World")
    print("2. Goodbye World")
    print("3. Goodbye Person")
    print("4. Good Teacher")
    print("5. forLoop")
    print("6. whileLoop")
    print("7. string Loop")
    print("8. Conver to ascii")
    print("9. Encode a string")
    print("x. To Exit")
    answer = input("Enter an option ")

    # Defining functions for each set of code
    def my_function1():
        print("Hello World") 

    def my_function2():
        print("Hello World")
        input("------> Program paused - press enter to continue")
        print("Goodbye World")

    def my_function3():
        print("Hello")
        username = input("What is your name ? ")
        print("Goodbye " + username)

    def my_function4():
        username = input("Teacher's name (try Mr Horan) ")
        x = "Mr Horan"

        if username == x:
            print("You are lucky, he is a great teacher.")
        else:
            print(username + " is an ok teacher")

    def my_function5():
        for x in range(1, 500):
            print(x)

    def my_function6():
        x = input("What is the name of this subject ")
        y = "IST"

        while x != y:
            print("Not Correct - try again")
            x = input("What is the name of this subject ")

        else: 
            print("")
            print("")
            print(" Congratulations!!")
            print("")
            print("")
    
    def my_function7():
        word = input("What is your string? ")
        for x in word:
            print(x)
    
    def my_function8():
        word = input("What is your string? ")

        for x in word:
            print(x, "=", ord(x))
    
    def my_function9 ():
        word = input("What is your string? ")
        ascii = ""

        for x in word:
            encode = chr(ord(x)+1)
            print(x, "=", encode)
            ascii += encode
            print(ascii)

    def my_functionInvalid():
        print("invalid option")

    def my_functionStart():
        print("")
        print("----Start of Output ---------------------------")
        print("")

    def my_functionEnd():
        print("")
        print("----End of Output -----------------------------")

    def my_functionRestart():
        print("")
        print("")
        print("")
        input("Press Enter to continue")

    # Function for clearing the code and restarting    
    def clear():
        from os import system, name
        if name == 'nt':
            return my_menu() #makes it recurring
        else:
            return my_menu() #makes it recurring

    # if...else statements for the output of each function (e.g. hello world- option 1, goodbye world- option2, etc.)

    # Hello World option
    if answer == "1":
        my_functionStart()
        my_function1()
        my_functionEnd()
        my_functionRestart()
        clear()
    # Goodbye World option
    elif answer == "2":
        my_functionStart()
        my_function2()
        my_functionEnd()
        my_functionRestart()
        clear()
    
    # Goodbye Person option
    elif answer == "3":
        my_functionStart()
        my_function3()
        my_functionEnd()
        my_functionRestart()
        clear()
    
    # Good Teacher option    
    elif answer == "4":
        my_functionStart()
        my_function4()
        my_functionEnd()
        my_functionRestart()
        clear()
    
    # For Loop option
    elif answer == "5":
        my_functionStart()
        my_function5()
        my_functionEnd()
        my_functionRestart()
        clear()
        
    # While Loop option   
    elif answer == "6":
        my_functionStart()
        my_function6()
        my_functionEnd()
        my_functionRestart()
        clear()
    
    # String Loop option
    elif answer == "7":
        my_functionStart()
        my_function7()
        my_functionEnd()
        my_functionRestart()
        clear()
    
    # Convert To ASCII option
    elif answer == "8":
        my_functionStart()
        my_function8()
        my_functionEnd()
        my_functionRestart()
        clear()
    
    # Encode a String option
    elif answer == "9":
        my_functionStart()
        my_function9()
        my_functionEnd()
        my_functionRestart()
        clear()

    # Breaks the code
    elif answer == "x":
        my_functionStart()
        my_functionEnd()
        my_functionRestart()

    else:
        my_functionStart()
        my_functionInvalid()
        my_functionEnd()
        my_functionRestart()
        clear()

#prints the whole menu function for the code to begin
my_menu()  

