print(" ------------------------------------------------")
print("|                                                |")
print("|    09convertToASCII                            |")
print("|    Name : Nikhita Arora                        |")
print("|    Version : 01                                |")
print("|                                                |")
print(" ------------------------------------------------")

word = input("What is your string? ")

for x in word:
    print(x, "=", ord(x))