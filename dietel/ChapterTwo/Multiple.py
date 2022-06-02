firstNumber = int(input("Enter first number: "))
secondNumber = int(input("Enter second number: "))
tripledFirst = firstNumber ** 3
doubledSecond = secondNumber ** 2

if tripledFirst % doubledSecond == 0:
    print(tripledFirst, 'is a multiple of', doubledSecond)
else:
    print(tripledFirst, 'is not a multiple of', doubledSecond)
