#with open ("hello.txt", mode="w", encoding="utf-8") as file:

file = open ("hello.txt", mode="w", encoding="utf-8")
file.write("I love writing\n")
file.write("I love writing\n")
file.writelines(["I am prone to violence", "i am prone to violence"])
file.close()


__all__ = ['add' 'sub']

def add(a, b):
    return a + b


def sub(a, b):
    return a - b


print("Mod 1", __name__)

if __name__ == '__main__':
    print("I am invisible to other modules")
    print("Mod 1", __name__)
