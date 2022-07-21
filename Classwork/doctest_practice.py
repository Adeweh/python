import collections
import doctest


def add(a, b):
    """
    >>> add (3, 5)
    8
     >>> add (3, "Hi")
     Traceback (most recent call last):


    TypeError: unsupported operand type(s) for +: 'int' and 'str'
     """

    return a + b


if __name__ == '__main__':
    doctest.testmod()

collections.Counter("hello")
 