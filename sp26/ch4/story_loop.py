print("Welcome to Treasure Island! You have scurvy!\n"
    "You have 10 days (moves) to find fruit before you die.\n")

# for day_number in [0, 1, 2, 3,...]:
for day_number in range(11):
    print("Day", day_number, "(you have", 10-day_number, "days left)")

# DON'T DO IT THIS WAY:
# for day_number in range(11):
#     for days_left in range(10, -1, -1):
#         print("Day", day_number, "(you have", days_left, "days left)")
