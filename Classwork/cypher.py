import string

abc = string.ascii_lowercase

word = input("Enter a word to encode: ")

while not word.isalpha():
    word = input("Invalid Entry. Enter a word to encode: ")

key = (input("Enter a number for your key: "))
while not key.isdigit():
    key = input("Invalid Entry. Enter a number for your key: ")

trans = abc[int(key):] + abc[:int(key)]
cypher = word.translate(str.maketrans(abc, trans))

print("your encrypted message is ", cypher)

decrypt = cypher.translate(str.maketrans(trans, abc))

print("your decrypted message is ", decrypt)
