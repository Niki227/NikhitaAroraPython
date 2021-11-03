print(" ------------------------------------------------")
print("|                                                |")
print("|    10encodeAString                             |")
print("|    Name : Nikhita Arora                        |")
print("|    Version : 01                                |")
print("|                                                |")
print(" ------------------------------------------------")

word = input("What is your string? ")

ascii = ""

for x in word:
    encode = chr(ord(x)+1)
    print(x, "=", encode)
    ascii += encode
    print(ascii)

    





       