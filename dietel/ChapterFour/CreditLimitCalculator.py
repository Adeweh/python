newBalance = 0


accountNumber = eval(input("Enter customer's charge account or -1 to quit:  "))

while accountNumber != -1:
    beginningBalance = eval(input("Enter balance at the beginning of the month or -1 to quit: "))

    totalCharges = eval(input("Enter total of all items charged by the customer this month or -1 to quit: "))

    totalCredit = eval(input("Enter total of all credits applied to the customer's account this month or -1 to quit: "))

    allowedCredit = eval(input("Enter allowed credit limit or -1 to quit: "))

    newBalance = beginningBalance + totalCharges - totalCredit

    print("The new balance is: ", newBalance)

if newBalance > allowedCredit:
    print("Credit Limit Exceeded.")

    # accountNumber = eval(input("Enter customer's charge account or -1 to quit:  "))


