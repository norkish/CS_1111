import random

BOTTOM_NUMBER = 1
TOP_NUMBER = 100

num_guesses_so_far = 0

# Design and write a program that assigns a number (chosen by you)
correct_answer = random.randrange(BOTTOM_NUMBER, TOP_NUMBER)

user_guess = None

# While the user’s guess is not the hidden number
while user_guess != correct_answer:
    # between 1 and 10 to a variable and then prompts the user to guess
    # the number.
    user_guess = int(input("Guess a number between " + str(BOTTOM_NUMBER) +
                           " and " + str(TOP_NUMBER) + ": "))
    num_guesses_so_far = num_guesses_so_far + 1

    if user_guess == correct_answer:
        print("Congrats! You nailed it!")
        # exit()
    else:
        if user_guess < correct_answer:
            print("Too low")
        else:
            print("Too high")

    # Adapt the program to give the user 5 guesses.


print("You got it in", num_guesses_so_far, "guesses")
