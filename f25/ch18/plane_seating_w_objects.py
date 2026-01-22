NO_CHOICE = -1
DISPLAY_PASSENGERS = 0
DISPLAY_SEATING = 1
ADD_PASSENGER = 2
LOOKUP_PASSENGER = 3
QUIT = 4

PRINT_PASSENGER = 0
EDIT_PASSENGER = 1
DELETE_PASSENGER = 2
RETURN_TO_MAIN = 3

PLANE_ROWS = 10
PLANE_COLS = 6

passengers_list = []
seating_chart = [[None] * PLANE_COLS for row in range(PLANE_ROWS)]

class Seat:
    def __init__(self, row, col):
        self.row = row
        self.col = col

    def __str__(self):
        return "Row " + str(self.row) + " Col " + str(self.col)

class Passenger:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        self.num_bags = 0
        self.seat = None

    def print_passenger_information(self):
        print("Name:", self.fname, self.lname)
        print("# of bags:", self.num_bags)
        print("Seat assignment:", self.seat)


    def __str__(self):
        return self.lname + ", " + self.fname


def print_menu():
    print("""Please select from the following options:
    1. Display all passengers
    2. Display seating chart
    3. Add new passenger
    4. Lookup/edit/delete passenger
    5. Quit""")


def print_passenger_menu():
    print("""Please select from the following options:
    1. Print passenger data
    2. Edit passenger data
    3. Delete passenger
    4. Return to main menu
    """)


def solicit_choice(min_choice, max_choice):
    # assume input is 1-based and must be converted to 0-based
    choice = int(input("Selection: ")) - 1
    while choice < min_choice or choice > max_choice:
        choice = int(input("Selection: ")) - 1
    return choice


def display_passengers():
    print("DISPLAYING PASSENGER LIST")
    for i in range(len(passengers_list)):
        print(f"{i}.", passengers_list[i])


def display_seating():
    print("DISPLAYING SEATING CHART\n    ", end="")
    for col in range(PLANE_COLS):
        if col == PLANE_COLS // 2:
            print("   ", end="")
        print(" " + chr(ord('A') + col) + " ", end="")
    print()
    for row in range(PLANE_ROWS):
        print(row, " |", end="")
        for col in range(PLANE_COLS):
            if col == PLANE_COLS // 2:
                print("   ", end="")
            if seating_chart[row][col] is None:
                print(" ⊡ ", end="")
            else:
                print(" ▣ ", end="")
        print("|")
    print()


def add_passenger():
    print("ADDING NEW PASSENGER")
    if len(passengers_list) >= PLANE_COLS * PLANE_ROWS:
        print("UNABLE TO ADD PASSENGER")
    else:
        fname = input("First name: ")
        lname = input("Last name: ")
        new_passenger = Passenger(fname, lname)
        passengers_list.append(new_passenger)
        print("PASSENGER ADDED")


def lookup_passenger():
    print("LOOKING UP PASSENGER")
    # TODO: Get passenger object from list
    fname = input("First name: ")
    lname = input("Last name: ")

    passenger_found = None

    for i in range(len(passengers_list)):
        if passengers_list[i].fname == fname and \
            passengers_list[i].lname == lname:
            passenger_found = passengers_list[i]
            break

    if passenger_found is None:
        print("Passenger not found!")
        return

    choice = NO_CHOICE
    while choice != RETURN_TO_MAIN:
        print_passenger_menu()
        choice = solicit_choice(PRINT_PASSENGER, RETURN_TO_MAIN)

        if choice == PRINT_PASSENGER:
            passenger_found.print_passenger_information()
        elif choice == EDIT_PASSENGER:
            print("EDITING PASSENGER", passenger_found)
            fname = input("New first name (hit enter to keep same): ")
            if len(fname) != 0:
                passenger_found.fname = fname
            lname = input("New last name (hit enter to keep same): ")
            if len(lname) != 0:
                passenger_found.lname = lname
            num_bags_string = input("Number of bags (hit enter to keep same): ")
            if len(num_bags_string) != 0:
                passenger_found.num_bags = int(num_bags_string)
            row_string = input("Row  (hit enter to keep same): ")
            if len(row_string) != 0: # New seating assignment
                row = int(row_string)
                col = int(input("Column  (hit enter to keep same): "))

                # Check if seat is taken
                if seating_chart[row][col] is not None:
                    print("SEAT IS TAKEN!")
                    return
                else:
                    if passenger_found.seat is not None: # check if passenger has old seat assn
                        print("FREEING UP OLD SEAT")
                        # free up the old
                        seating_chart[passenger_found.seat.row][passenger_found.seat.col] = None
                    passenger_found.seat = Seat(row, col) # assign seat to passenger
                    seating_chart[row][col] = passenger_found # update seating chart

        elif choice == DELETE_PASSENGER:
            if passenger_found.seat is not None:
                # free up the old
                seating_chart[passenger_found.seat.row][passenger_found.seat.col] = None
            for i in range(len(passengers_list)):
                if passengers_list[i].fname == fname and \
                        passengers_list[i].lname == lname:
                    del passengers_list[i]
                    break

            choice = RETURN_TO_MAIN


def main():
    choice = NO_CHOICE
    while choice != QUIT:
        print_menu()
        choice = solicit_choice(DISPLAY_PASSENGERS, QUIT)

        if choice == DISPLAY_PASSENGERS:
            display_passengers()
        elif choice == DISPLAY_SEATING:
            display_seating()
        elif choice == ADD_PASSENGER:
            add_passenger()
        elif choice == LOOKUP_PASSENGER:
            lookup_passenger()


if __name__ == "__main__":
    main()
