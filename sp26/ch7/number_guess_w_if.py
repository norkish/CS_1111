import random

BOTTOM_NUMBER = 1
TOP_NUMBER = 100
NUM_GUESSES = 5

# Design and write a program that assigns a number (chosen by you)
correct_answer = random.randrange(BOTTOM_NUMBER, TOP_NUMBER)

for i in range(NUM_GUESSES):
    # between 1 and 10 to a variable and then prompts the user to guess
    # the number.
    user_guess = int(input("Guess a number between " + str(BOTTOM_NUMBER) +
                           " and " + str(TOP_NUMBER) + ": "))

    if user_guess == correct_answer:
        print("Congrats! You nailed it!")
        exit()
    else:
        if user_guess < correct_answer:
            print("Too low")
        else:
            print("Too high")

    # Adapt the program to give the user 5 guesses.


print("Correct answer was:", correct_answer)
