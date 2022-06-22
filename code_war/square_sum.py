# Complete the square sum function so that it squares each number passed into it and then sums the results together.
#
# For example, for [1, 2, 2] it should return 9 because 1^2 + 2^2 + 2^2 = 9.

def square_sum(numbers):
    out = []
    for number in numbers:
        out.append(number ** 2)
    return sum(out)


print(square_sum([1, 2, 2]))
