# Design and write a program that prompts the user for a date in
# January.
user_date = int(input("Input a date in January (an integer): "))

# Print out “True” or “False” based on whether the input
# number is a valid date in January (hint: there is no January 32
# and no January -1).

print("The date you entered when considered as a day in the month of January is...")
print(user_date >= 1 and user_date <= 31)
