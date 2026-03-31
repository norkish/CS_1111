# Write a program with a list of your closest friends.
closest_friends = ["Alice", "Bob", "Clarice", "Devin"]

count = 0

# Let the user check five different names.
while count < 5:
    # Prompt the user for a name.
    user_name = input("Enter a name: ")

    # Check if the name is in the list.
    if user_name in closest_friends:
        # Print out a message that says whether the name given is one of your friends.
        print(user_name, "is one of my closest friends!")
    else:
        print(user_name, "is not one of my closest friends.")
        add = input("Would you like to add them (Y/N)? ")
        if add == "Y":
            closest_friends.append(user_name)

    count = count + 1
