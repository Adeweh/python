# def avg(*args):
#     print(type(args))
#     return args


def avg(*args):
    total = 0
    # for i in args:
    #     total += 1
    # return total / len(args)
    return sum(args) / len(args)


print((avg(1, 2, 3, 4)))
print(avg(1, 2, 3))

lst = [1, 2, 3, 4, 5]
set_ = {1, 2, 3, 4, 5}
print(avg(*lst, *set_))


def add(a=0, b=0, c=0):
    return a + b + c


def add(**kwargs):
    for k, v in kwargs.items():
        print(k, "==>", v)


add(b=6, c=5, a=7)

# d = dict(b=6, c=5, a=7)
# print(d)
print(add())
