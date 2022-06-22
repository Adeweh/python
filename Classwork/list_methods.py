import random
lst = [1, 2, 3, 4]

random.seed(45)
rng = list(range(1, 100, 5))
print(rng)
# new = rng.copy()
# print(new)
#
# rng.append(1_000)
# rng.append([2, 3, 4])
# print(rng)
#
# rng.extend([2, 3, 4])
# print(rng)
#
# rng += [1, 2, 3]  # extend does the same thing as +=
# print(rng)
#
# rng.insert(0, 99)  # insert elements on any index of the list
# print(rng)
#
# popped = rng.pop()  # removes last element from list when you do not pass in an argument
# print(popped)
# print(rng)
#
# popped = rng.pop(2)  # removes last element from list using index
# print(popped)
# print(rng)
#
# rng.remove(2)
# print(rng)
#
# idx=rng.index(71)
# print(idx)
# print(rng)
#
# cnt = rng.count(1)
# print(cnt)
# print(rng)
#
# rng.clear()
# print(rng)

random.shuffle(rng)
print(rng)
print(random.choice(rng))
rng.sort()
print(rng)
rng.reverse()
print(rng)
rng.sort(reverse=False)
print(rng)

fruits = ["apple", "mango", "water melon", "cherry", "banana", "cucumber", "pineapple", "orange"]
fruits.sort()
print(fruits)

fruits.sort(key=len)
print(fruits)

fruits.sort(key=len, reverse=True)
print(fruits)




