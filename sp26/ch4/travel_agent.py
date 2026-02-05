# travel.py: You work for a travel agency in Pocatello.
# Write a program that lets the user choose 5 cities to
# visit, one at a time.

# They should start in Pocatello.
current_city = "Pocatello"

for i in range(5):
    # At each step, tell the user the city they are in, and
    print("You are currently in " + current_city + ".")
    current_city = input("Where to next? ")
    # prompt them for the next city they want to visit.
