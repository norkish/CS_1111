import random

NUM_ROUNDS = 3

ROCK = 0
PAPER = 1
SCISSORS = 2

TIE = 0

def convert_rps_to_string(num):
    if num == ROCK:
        return "ROCK"
    elif num == PAPER:
        return "PAPER"
    else:
        return "SCISSORS"


def randomly_select_rps():
    random_number = random.randrange(3)
    return random_number


def solicit_rps_from_user():
    user_input = None
    while user_input != 'r' and user_input != 'p' and user_input != 's':
        user_input = input("r, p, or s? ")

    if user_input == 'r':
        return ROCK
    elif user_input == 'p':
        return PAPER
    elif user_input == 's':
        return SCISSORS


def determine_winner(p1_choice, p2_choice):
    if p1_choice == ROCK:
        if p2_choice == ROCK:
            return TIE
        elif p2_choice == PAPER:
            return 2
        else: #p2 chose scissors
            return 1
    elif p1_choice == PAPER:
        if p2_choice == ROCK:
            return 1
        elif p2_choice == PAPER:
            return TIE
        else: #p2 chose scissors
            return 2
    elif p1_choice == SCISSORS:
        if p2_choice == ROCK:
            return 2
        elif p2_choice == PAPER:
            return 1
        else: #p2 chose scissors
            return TIE


p1_wins = 0
p2_wins = 0
ties = 0

play_again = True
round_number = 0
while play_again:
# for round_number in range(NUM_ROUNDS):
    print("ROUND #", round_number)
    winner = TIE
    while winner == TIE:
        # two players
        # each player randomly selects one of three options
        player_1_selection = solicit_rps_from_user()
        player_2_selection = randomly_select_rps()
        print("Computer chose", convert_rps_to_string(player_2_selection))

        # print("Player 1 chose", convert_rps_to_string(player_1_selection))
        # print("Player 2 chose", convert_rps_to_string(player_2_selection))

        # compare selections to determine winner
        winner = determine_winner(player_1_selection, player_2_selection)

        if winner == TIE:
            print("TIE")
        elif winner == 1:
            print("Player 1 WINS!")
            p1_wins = p1_wins + 1
        elif winner == 2:
            print("Player 2 WINS!")
            p2_wins = p2_wins + 1


    round_number = round_number + 1
    play_again = input("Play again (Y/N)? ") == "Y"

print("Player 1 won", p1_wins, "rounds (", p1_wins/NUM_ROUNDS, "%)")
print("Player 2 won", p2_wins, "rounds (", p2_wins/NUM_ROUNDS, "%)")
print("There were", ties, "ties (", ties/NUM_ROUNDS, "%)")
