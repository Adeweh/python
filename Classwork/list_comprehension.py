y = [i for i in range(1, 11)]

print(y)

y = [i for i in range(1, 11) if i % 2 == 0]

print(y)

y = "even" if 4 % 2 == 0 else "odd"

print(y)

y = [i ** 2 if i % 2 == 0 else i for i in range(1, 11)]

print(y)

lst = [int(input(f"Enter a student {i}'s score: ")) for i in range(1, 6)]

print(lst)
print(sum(lst))
print(max(lst))
print("Average = ", sum(lst) / len(lst))
