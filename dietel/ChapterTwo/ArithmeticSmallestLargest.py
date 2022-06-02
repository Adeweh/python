firstNumber = eval(input("Enter first number: "))
secondNumber = (input("Enter second number: "))
thirdNumber = eval(input("Enter third number: "))
add = firstNumber + secondNumber + thirdNumber
average = add / 3
product = firstNumber * secondNumber * thirdNumber

largest = firstNumber
if secondNumber > largest:
    largest = secondNumber
if thirdNumber > largest:
    largest = thirdNumber

smallest = firstNumber
if secondNumber < smallest:
    smallest = secondNumber
if thirdNumber < smallest:
    smallest = thirdNumber

print(add)
print(average)
print(product)
print(largest)
print(smallest)


