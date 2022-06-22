# d = dict(a=1, b=2, c=3)
#
# print(d.fromkeys('abcde', 0))
#
# print({}.fromkeys('abcde', list(range(1))))
#
# d.setdefault('d', 8)
# print(d)


def sum_num(a: int, b: int) -> int:
    """Adds two numbers"""
    return a + b


def operate(fn, x, y):
    fn(x, y)


print(sum_num(3, 6))

print(operate(sum_num, 2, 3))
print(operate(subtract, 5, 2))
print(operate(lambda x, y: x * y, 3, 4))

# print(sum_num.__name__)
# print(sum_num.__doc__)
# print(sum_num.__annotations__)
