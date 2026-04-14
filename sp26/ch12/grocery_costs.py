# Use a dictionary to keep track of the prices of items
costs_by_food = {
    "apple": 0.99,
    "banana": 0.59,
    "bread": 2.49,
    "milk": 3.19,
    "eggs": 2.79,
    "cheese": 4.49,
    "chicken": 8.99,
    "rice": 1.29,
    "pasta": 1.09,
    "chocolate": 4.50
}

# Use a dictionary to keep track of scanned items and their quantities
shopping_cart = {}

user_choice = None
# Write a program that loops, allowing the user to select one of three options:
while user_choice != "CHECKOUT":
    user_choice = input("Type 'INPUT' item, 'REMOVE' item, 'VIEW' cart, or 'CHECKOUT': ")
    if user_choice == "INPUT":
        print("CHOICES: ", list(costs_by_food.keys()))
        food_selection = input("Type food name: ")
        if food_selection not in costs_by_food:
            print(food_selection + " not in database")
        else:
            # add item to shopping cart
            if food_selection not in shopping_cart:
                shopping_cart[food_selection] = 0
            shopping_cart[food_selection] += 1

    elif user_choice == "REMOVE":
        print("CHOICES: ", list(shopping_cart.keys()))
        food_selection = input("Type food name: ")
        if food_selection not in shopping_cart:
            print(food_selection + " not in shopping cart")
        else:
            # add item to shopping cart
            shopping_cart[food_selection] -= 1
            if shopping_cart[food_selection] == 0:
                del shopping_cart[food_selection]
    elif user_choice == "VIEW":
        print(shopping_cart)


# When the user selects checkout, print out a receipt with all items,
# their quantities, and the total cost
total_cost = 0.0

for (food_item, quantity) in shopping_cart.items():
    item_cost = costs_by_food[food_item]
    total_item_cost = quantity * item_cost
    print(food_item + " (@$" + str(item_cost) + ") x " + str(quantity) + " = $" + str(total_item_cost))
    total_cost += total_item_cost

print("TOTAL COST: $" + str(total_cost))
