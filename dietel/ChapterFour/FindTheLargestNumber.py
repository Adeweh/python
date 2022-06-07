counter = 1
largest = 0

while counter <= 10:

    number = int(input("Enter an integer: "))

    if number > largest:
        largest = number

        print("The Largest Integer is ", largest)
