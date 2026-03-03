import random

NUM_EXPERIMENTS = 10000

tallies = 0
for i in range(NUM_EXPERIMENTS):
    # For each experiment 
    roll_value = 0 # zero out our die
    # while I don't have a six
    while roll_value != 6:
        # roll the die
        roll_value = random.randrange(1,7)
        print("You rolled", roll_value)

        # add a tally mark (this accumulates across all experiments)
        tallies = tallies + 1

print("It took on average", tallies//NUM_EXPERIMENTS, "rolls to get a six")
