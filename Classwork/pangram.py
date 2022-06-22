import string


def is_pangram(s):
    alphabet = string.ascii_lowercase
    s = s.lower()

    char_array = [alphabet[i] for i in alphabet]
    letter_count = []

    for i in char_array:
        count = s.count(i)
        letter_count.append(count)

    dict_ = dict(zip(char_array, letter_count))

    for val in dict_.values():
        if val == 0:
            return False

    return True

# return set(string.ascii_lowercase <= set(s.lower()))
