from Tamagotchi import Tamagotchi

pet1 = Tamagotchi("Tom")

while(True):
    print(pet1.name + " has a hunger level of " + str(pet1.hunger))

    user_choice = input("Eat OR Do nothing? ")
    if user_choice == "Eat":
        pet1.eat()
    else:
        pet1.get_hungry()
