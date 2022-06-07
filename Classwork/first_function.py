"""
celsius_to_fahrenheit(celsius_float) -> float:
converts celsius to fahrenheit
:param celsius float
:return celsius_float"""


def celsius_to_fahrenheit(celsius_float) -> float:
    return celsius_float * 1.8 + 32


fahrenheit = celsius_to_fahrenheit(100)
print(fahrenheit)

help(celsius_to_fahrenheit)



