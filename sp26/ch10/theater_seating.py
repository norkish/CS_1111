# The theater has a list of seat numbers and names
theater_list = ["Paul", "Paige", "Ian", "Austin", "Reagan", "Oceane", "Angelo", "Jenna"]

# Your program should do this 6 times
for i in range(6):
    # Create a program that prompts the user for their seat number
    seat_num = int(input("Enter seat number: "))

    # Print out the name of the user at that seat number
    print(seat_num, ":", theater_list[seat_num])

    # Prompts the user for a new name to assign to the seat
    new_name = input("Enter new name: ")
    theater_list[seat_num] = new_name

    print("New seating chart: ")
    for i in range(len(theater_list)):
        print(i, ":", theater_list[i])
