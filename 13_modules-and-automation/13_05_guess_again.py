# Re-create the guess-my-number game from scratch. Don't peek!
# This time, give your players only a certain amount of tries 
# before they lose.

num_attempts = 5
number = 7

while num_attempts > 0:
    if int(input("Enter your guess\n")) == number:
        print("You guessed the number")

    else:
        print("Guess again")

    num_attempts -= 1