# Write a function which calculates the average of the numbers in a given list.
#
# Note: Empty arrays should return 0.

def find_average(numbers):
    return sum(numbers) // len(numbers)
    pass


print(find_average([7, 6, 4, 22, 9, 55, 10]))
