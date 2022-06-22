def get_digit(number, position):
    return number // (10 ** position) % 10


num = 234
pos = 1


ans = get_digit(num, pos)
print(ans)
