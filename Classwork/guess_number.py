import random
"""correct_guess = random.randint(0, 100)
count = 0
while count < 5:
    userGuess = int(input("Guess a number between 0 and 100: "))
    if guess < 0 or guess > 100:
    print('Out of range...')
    break
    
    if userGuess < correct_guess:
        print('Too low, try again')
    elif userGuess > correct_guess:
        print('Too high, try again')
    else:
        print("Awesome, you are correct")
        break

    count += 1
else:
    print("you tried, but you can never make it")
    print("the correct answer is: ", correct_guess)"""
random = random.randint(0, 10)
count = 0

while count < 5:
    userInput = int(input("Guess a number: "))
    count += 1

    if userInput > random:
        print('Too high Bro')
    elif userInput < random:
        print('Too low Bro')
    else:
        userInput == random
        print('Awesome, You are correct')







