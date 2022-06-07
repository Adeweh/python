print("number\t\tsquare\t\tcube")

numberZero = 0
numberOne = 1
squaredOne = numberOne * numberOne
cubeOne = numberOne * numberOne * numberOne
numberTwo = 2
squaredTwo = numberTwo * numberTwo
cubeTwo = numberTwo * numberTwo * numberTwo
numberThree = 3
squaredThree = numberThree * numberThree
cubeThree = numberThree * numberThree * numberThree
numberFour = 4
squaredFour = numberFour * numberFour
cubeFour = numberFour * numberFour * numberFour
numberFive = 5
squaredFive = numberFive * numberFive
cubeFive = numberFive * numberFive * numberFive

print(numberZero, "\t\t\t", numberZero, "\t\t\t", numberZero)
print(numberOne, "\t\t\t", squaredOne, "\t\t\t", cubeOne)
print(numberTwo, "\t\t\t", squaredTwo, "\t\t\t", cubeTwo)
print(numberThree, "\t\t\t", squaredThree, "\t\t\t", "{:<10}" .format(cubeThree))
print(numberFour, "\t\t\t", squaredFour, "\t\t", "{:<11}".format(cubeFour))
print(numberFive, "\t\t\t", squaredFive, "\t\t", "{:<10}" .format(cubeFive))

