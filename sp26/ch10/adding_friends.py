# Live Coding Demo— Write a program that solicits a
# list of friends from the user. Save the list in a
# variable with a good variable name. Print the
# list and then print the length of the list.

friend_list = []

name = "TO BE REPLACED"
while len(name) > 0:
    name = input("Enter friend's name (Hit ENTER when done): ")
    if len(name) > 0:
        friend_list.append(name)

print(friend_list)
