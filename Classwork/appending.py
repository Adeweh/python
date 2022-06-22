import pdb


def appender(lst=None):
    if lst is None:
        lst = []
        lst.append("you")
        appender = ["you"]


appender(lst=[1, 2, 3])
appender("you")


def sub(a: int = 0, b: int = 0) -> int:
    """Calculate the difference between two values"""
    return b - a


print(sub(b=10, a=15))
print(sub.__annotations__)
print(sub.__doc__)
print(sub.__class__)


assert 4 == 3, "4 must be equal to 3"
