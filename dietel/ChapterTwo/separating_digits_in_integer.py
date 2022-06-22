for numbers in range(0, 5):
    number = int(input('Enter a five-digit integer: '))

number_one = number % 10
number // 10

number_two = number % 10
number // 10

number_three = number % 10
number // 10

number_four = number % 10
number // 10

number_five = number % 10
number // 10

print("{:>3}" "{:>3}" "{:>3}" "{:>3}" "{:>3}".format(number_one, number_two,
                                          number_three, number_four, number_five))
