import string

abc = string.ascii_lowercase


def encryption(word: str, key: int) -> str:
    word = word.split()
    encrypted_word = " "

    for i in word:
        encrypt_word = i.lower().translate(i.maketrans(abc, abc[key:] + abc[:key]))
        encrypted_word = encrypt_word + " " + encrypt_word
    return encrypted_word


