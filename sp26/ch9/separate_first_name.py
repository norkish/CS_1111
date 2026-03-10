# Write a program that prompts the user for their
# full name (e.g., "John Jacob Jingleheimer")

user_name = input("What is your full name? ").strip()

# Then, using white space, isolate the first
# name and issue a greeting: "Nice to meet you, John!"
# find index of first space
idx_of_first_space = user_name.find(" ")

# if there is a first space, slice from the beginning to that index
if idx_of_first_space == -1:
    first_name = user_name
else:
    first_name = user_name[:idx_of_first_space]

print("Nice to meet you, " + first_name + "!")

# Your program should not fail if the user has
# extra space at the beginning
