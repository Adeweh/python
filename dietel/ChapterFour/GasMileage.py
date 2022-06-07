totalMilesPerGallon = 0.0

miles = eval(input("Enter miles driven or -1 to quit: "))


gallons= eval(input("Enter gallons used or -1 to quit: "))

while miles != -1 and gallons != -1:
    milesPerGallon = miles / gallons

    print("Miles per gallon obtained for this trip is: ", milesPerGallon)

    totalMilesPerGallon += milesPerGallon

    print("Combined Miles per gallons obtained for all trips up to this point is: ", totalMilesPerGallon)

    miles = eval(input("Enter miles driven or -1 to quit: "))

    gallons = eval(input("Enter gallons used or -1 to quit: "))





