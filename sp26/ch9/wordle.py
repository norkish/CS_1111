#NOTE THIS DOES NOT CORRECTLY HANDLE ANSWERS OR GUESSES WITH REPEAT CHARACTERS
#ASSUMES ANSWER AND GUESS ARE STRINGS OF SAME LENGTH

MAX_GUESSES = 6

answer = 'fight'

guess_number = 0
while guess_number < MAX_GUESSES:
    user_guess = input("").lower()

    for i in range(len(user_guess)):
        # check for correct chars in correct position
        if user_guess[i] == answer[i]:
            print("*", end = "")
        else:
            # check if char is in the answer at all
            if user_guess[i] in answer:
                print("!", end = "")
            else:
                print(" ", end = "")

    print()
    guess_number += 1
  
