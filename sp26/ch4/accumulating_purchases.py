# accumulator pattern

# assign a variable to a number
total_cost = 0.0

item_count = int(input("How many items? "))

# then add to it over the course of the program
# Use a for loop to add up the cost of multiple items
# Start by hard coding the number of items to 3 items
for items in range(item_count):
    # You should get the cost of the items each as an input from the user
    item_cost = float(input("What is the cost of the next item? $"))
    total_cost = total_cost + item_cost

print("Total cost is: $", total_cost)
