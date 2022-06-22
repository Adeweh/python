list = [1, 2, [4, 5], 7]
lst_copy = list[:]

print(lst_copy)

lst_copy[0] = 5
print(lst_copy)

lst_copy[2][0] = 10
print(lst_copy)

lst = (1, 2, [3, 4])  # tuples are immutable
lst[2].append(0)
print(lst)
