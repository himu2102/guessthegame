import random
import time

number = random.randint(1, 200)

def intro():
    print("May I ask you for your name?")
    name = input()
    print(name + ", we are going to play a game. I am thinking of a number between 1 and 200")
    time.sleep(.5)
    print("Go ahead. Guess!")
    return name  # Return the 'name' variable to pass it to the pick() function.

def pick(name):  # Accept 'name' as an argument.
    guessesTaken = 0
    while guessesTaken < 6:
        time.sleep(.25)
        enter = input("Guess: ")
        try:
            guess = int(enter)

            if guess <= 200 and guess >= 1:
                guessesTaken = guessesTaken + 1
                if guessesTaken < 6:
                    if guess < number:
                        print("The guess of the number that you have entered is too low")
                    elif guess > number:  # Use 'elif' instead of 'if' to avoid redundant checks.
                        print("The guess of the number that you have entered is too high")
                    else:
                        time.sleep(.5)
                        print("Try Again!")
                if guess == number:
                    break
            elif guess > 200 or guess < 1:
                print("Silly Goose! That number isn't in the range!")
                time.sleep(.25)
                print("Please enter a number between 1 and 200")
        except:
            print("I don't think that " + enter + " is a number. Sorry")

    if guess == number:
        guessesTaken = str(guessesTaken)
        print('Good job, ' + name + '! You guessed my number in ' + guessesTaken + ' guesses!')
    else:
        print('Nope. The number I was thinking of was ' + str(number))

playagain = "yes"
while playagain == "yes" or playagain == "y" or playagain == "Yes":
    player_name = intro()  # Capture the 'name' returned by the intro() function.
    pick(player_name)  # Pass the 'name' to the pick() function.
    print("Do you want to play again?")
    playagain = input()
