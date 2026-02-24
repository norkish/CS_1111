import random

BOTTOM_NUMBER = 1
TOP_NUMBER = 20
NUM_GUESSES = 5

# Design and write a program that assigns a number (chosen by you)
correct_answer = random.randrange(BOTTOM_NUMBER, TOP_NUMBER)

for i in range(NUM_GUESSES):
    # between 1 and 10 to a variable and then prompts the user to guess
    # the number.
    user_guess = int(input("Guess a number between " + str(BOTTOM_NUMBER) +
                           " and " + str(TOP_NUMBER) + ": "))

    # Print out “True” or “False” based on whether the guessed number
    # equaled the number you assigned.
    print("Guess was high: ", user_guess > correct_answer)
    print("Guess was correct: ", user_guess == correct_answer)
    print("Guess was low: ", user_guess < correct_answer)

    # Adapt the program to give the user 5 guesses.


print("Correct answer was:", correct_answer)
