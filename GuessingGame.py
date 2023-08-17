# Guessing Game
import random
Proceed = True
while Proceed == True:
    print("-------------------------------")
    print("Welcome to Guessing Game")
    print("You have 5 chances to guess")
    print("If you guess it right, you win")
    print("If you guess it wrong, you lose")
    print("Let's start the game")
    print("-------------------------------")
    Guess = random.randint(1, 100)
    Chance = 0
    while Chance < 5:
        Guessed = int(input("Enter your guess (Between 1 to 100): "))
        Chance += 1

        if Guessed == Guess:
            print("You guessed it right")
            break
        elif Guessed > Guess:
            print("You guessed it High")
            continue
        elif Guessed < Guess:
            print("You guessed it Low")
            continue
    else:
        print("-------------------------------")
        print("You are out of chances")
        print("The number was", Guess)
        print("-------------------------------")
    print("Do you want to play again?")
    print("Press 1 to play again")
    print("Press 2 to exit")
    Proceed = int(input("Enter your choice: "))
    if Proceed == 1:
        Proceed = True
    elif Proceed == 2:
        Proceed = False
    else:
        print("Invalid Input")
        break
print("-------------------------------")
print("Thank you for playing this game")
print("Have a nice day")
print("By Wakil Ahmad Hamidi")
print("-------------------------------")