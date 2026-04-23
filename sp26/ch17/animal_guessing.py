from Animal import Animal

# Write a program with an animal class in which the computer asks
# the user to think of an animal (one that appears in its database)

# Used an LLM to create the database from our class definition
animal_list = [
    Animal('Lion', 'Mammal', 4, ['Tan', 'Gold'], False, False, False, False),
    Animal('Bald Eagle', 'Bird', 2, ['Brown', 'White'], True, False, True, True),
    Animal('Goldfish', 'Fish', 0, ['Orange'], False, True, True, False),
    Animal('Ball Python', 'Reptile', 0, ['Brown', 'Black'], False, True, True, False),
    Animal('African Elephant', 'Mammal', 4, ['Grey'], False, False, False, False),
    Animal('Emperor Penguin', 'Bird', 2, ['Black', 'White'], True, False, True, False),
    Animal('Nile Crocodile', 'Reptile', 4, ['Olive', 'Grey'], False, True, True, False),
    Animal('Monarch Butterfly', 'Insect', 6, ['Orange', 'Black'], False, False, True, True),
    Animal('Fruit Bat', 'Mammal', 2, ['Black', 'Brown'], False, False, False, True),
    Animal('Common Ostrich', 'Bird', 2, ['Black', 'Grey'], True, False, True, False),
    Animal('Atlantic Salmon', 'Fish', 0, ['Silver'], False, True, True, False),
    Animal('American Bullfrog', 'Amphibian', 4, ['Green'], False, False, True, False),
    Animal('Macaw', 'Bird', 2, ['Red', 'Blue', 'Yellow'], True, False, True, True),
    Animal('Grey Wolf', 'Mammal', 4, ['Grey', 'White'], False, False, False, False),
    Animal('Green Sea Turtle', 'Reptile', 4, ['Green', 'Brown'], False, True, True, False),
    Animal('Great White Shark', 'Fish', 0, ['Grey', 'White'], False, True, False, False),
    Animal('Red Kangaroo', 'Mammal', 2, ['Red', 'Tan'], False, False, False, False),
    Animal('Honey Bee', 'Insect', 6, ['Yellow', 'Black'], False, False, True, True),
    Animal('Great Horned Owl', 'Bird', 2, ['Mottled Brown'], True, False, True, True),
    Animal('Giraffe', 'Mammal', 4, ['Orange', 'White'], False, False, False, False),
    Animal('Mallard Duck', 'Bird', 2, ['Green', 'Brown'], True, False, True, True),
    Animal('Clydesdale Horse', 'Mammal', 4, ['Brown', 'White'], False, False, False, False),
    Animal('Mountain Gorilla', 'Mammal', 2, ['Black'], False, False, False, False),
    Animal('Ruby-throated Hummingbird', 'Bird', 2, ['Green', 'Red'], True, False, True, True),
    Animal('Veiled Chameleon', 'Reptile', 4, ['Green', 'Yellow'], False, True, True, False),
    Animal('Grizzly Bear', 'Mammal', 4, ['Brown'], False, False, False, False),
    Animal('Platypus', 'Mammal', 4, ['Brown'], False, False, True, False),
    Animal('Komodo Dragon', 'Reptile', 4, ['Grey', 'Tan'], False, True, True, False),
    Animal('Blue Whale', 'Mammal', 0, ['Blue', 'Grey'], False, False, False, False),
    Animal('Cheetah', 'Mammal', 4, ['Tan', 'Black'], False, False, False, False),
    Animal('Red Fox', 'Mammal', 4, ['Red', 'White'], False, False, False, False),
    Animal('Chicken', 'Bird', 2, ['White', 'Red'], True, False, True, False),
    Animal('Cobra', 'Reptile', 0, ['Black', 'Tan'], False, True, True, False),
    Animal('Polar Bear', 'Mammal', 4, ['White'], False, False, False, False),
    Animal('Chimpanzee', 'Mammal', 2, ['Black'], False, False, False, False),
    Animal('Giant Panda', 'Mammal', 4, ['Black', 'White'], False, False, False, False),
    Animal('Zebra', 'Mammal', 4, ['Black', 'White'], False, False, False, False),
    Animal('Tiger', 'Mammal', 4, ['Orange', 'Black'], False, False, False, False),
    Animal('Red-tailed Hawk', 'Bird', 2, ['Brown', 'Red'], True, False, True, True),
    Animal('Clownfish', 'Fish', 0, ['Orange', 'White'], False, True, True, False),
    Animal('Rhinoceros', 'Mammal', 4, ['Grey'], False, False, False, False),
    Animal('Hippopotamus', 'Mammal', 4, ['Grey'], False, False, False, False),
    Animal('Flamingo', 'Bird', 2, ['Pink'], True, False, True, True),
    Animal('Koala', 'Mammal', 4, ['Grey'], False, False, False, False),
    Animal('Sloth', 'Mammal', 4, ['Grey', 'Brown'], False, False, False, False),
    Animal('Orca', 'Mammal', 0, ['Black', 'White'], False, False, False, False),
    Animal('Woodpecker', 'Bird', 2, ['Black', 'White', 'Red'], True, False, True, True),
    Animal('Iguana', 'Reptile', 4, ['Green'], False, True, True, False),
    Animal('Plains Bison', 'Mammal', 4, ['Dark Brown'], False, False, False, False),
    Animal('Moose', 'Mammal', 4, ['Brown'], False, False, False, False),
    Animal('Leopard', 'Mammal', 4, ['Yellow', 'Black'], False, False, False, False),
    Animal('Wolverine', 'Mammal', 4, ['Brown', 'Tan'], False, False, False, False),
    Animal('Seahorse', 'Fish', 0, ['Yellow', 'Tan'], False, False, True, False),
    Animal('Pelican', 'Bird', 2, ['White'], True, False, True, True),
    Animal('Box Turtle', 'Reptile', 4, ['Brown', 'Yellow'], False, True, True, False),
    Animal('Gila Monster', 'Reptile', 4, ['Orange', 'Black'], False, True, True, False),
    Animal('Snowy Owl', 'Bird', 2, ['White'], True, False, True, True),
    Animal('Meerkat', 'Mammal', 4, ['Tan'], False, False, False, False),
    Animal('Walrus', 'Mammal', 0, ['Brown'], False, False, False, False),
    Animal('Rattlesnake', 'Reptile', 0, ['Brown', 'Grey'], False, True, True, False),
    Animal('Peacock', 'Bird', 2, ['Blue', 'Green'], True, False, True, True),
    Animal('Lemur', 'Mammal', 4, ['Grey', 'Black', 'White'], False, False, False, False),
    Animal('Orangutan', 'Mammal', 2, ['Orange'], False, False, False, False),
    Animal('Swordfish', 'Fish', 0, ['Silver', 'Blue'], False, True, True, False),
    Animal('Toad', 'Amphibian', 4, ['Brown'], False, False, True, False),
    Animal('Peregrine Falcon', 'Bird', 2, ['Grey', 'White'], True, False, True, True),
    Animal('Hyena', 'Mammal', 4, ['Tan', 'Spotted'], False, False, False, False),
    Animal('Ocelot', 'Mammal', 4, ['Tan', 'Black'], False, False, False, False),
    Animal('Manta Ray', 'Fish', 0, ['Grey', 'White'], False, False, True, False),
    Animal('Albatross', 'Bird', 2, ['White', 'Black'], True, False, True, True),
    Animal('Tuna', 'Fish', 0, ['Blue', 'Silver'], False, True, True, False),
    Animal('Beaver', 'Mammal', 4, ['Brown'], False, False, False, False),
    Animal('Porcupine', 'Mammal', 4, ['Black', 'White'], False, False, False, False),
    Animal('Raven', 'Bird', 2, ['Black'], True, False, True, True),
    Animal('Badger', 'Mammal', 4, ['Black', 'White'], False, False, False, False),
    Animal('Armadillo', 'Mammal', 4, ['Grey'], False, True, False, False),
    Animal('Manatee', 'Mammal', 0, ['Grey'], False, False, False, False),
    Animal('Emu', 'Bird', 2, ['Brown'], True, False, True, False),
    Animal('Coyote', 'Mammal', 4, ['Tan', 'Grey'], False, False, False, False),
    Animal('Stingray', 'Fish', 0, ['Grey'], False, False, True, False),
    Animal('Kingfisher', 'Bird', 2, ['Blue', 'Orange'], True, False, True, True),
    Animal('Capybara', 'Mammal', 4, ['Brown'], False, False, False, False),
    Animal('Puffin', 'Bird', 2, ['Black', 'White', 'Orange'], True, False, True, True),
    Animal('Spider Monkey', 'Mammal', 4, ['Black', 'Brown'], False, False, False, False),
    Animal('Barracuda', 'Fish', 0, ['Silver'], False, True, True, False),
    Animal('Anaconda', 'Reptile', 0, ['Green', 'Black'], False, True, True, False),
    Animal('Vulture', 'Bird', 2, ['Black', 'Brown'], True, False, True, True),
    Animal('Lynx', 'Mammal', 4, ['Tan', 'Grey'], False, False, False, False),
    Animal('Aardvark', 'Mammal', 4, ['Tan'], False, False, False, False),
    Animal('Eel', 'Fish', 0, ['Black', 'Grey'], False, True, True, False),
    Animal('Mongoose', 'Mammal', 4, ['Brown'], False, False, False, False),
    Animal('Wombat', 'Mammal', 4, ['Grey', 'Brown'], False, False, False, False),
    Animal('Kestrel', 'Bird', 2, ['Brown', 'Grey'], True, False, True, True),
    Animal('Hamster', 'Mammal', 4, ['Tan', 'White'], False, False, False, False),
    Animal('Otter', 'Mammal', 4, ['Brown'], False, False, False, False),
    Animal('Turkey', 'Bird', 2, ['Brown', 'Red'], True, False, True, True),
    Animal('Gecko', 'Reptile', 4, ['Green', 'Spotted'], False, True, True, False),
    Animal('Skunk', 'Mammal', 4, ['Black', 'White'], False, False, False, False),
    Animal('Hedgehog', 'Mammal', 4, ['Brown', 'White'], False, False, False, False),
    Animal('Piranha', 'Fish', 0, ['Silver', 'Red'], False, True, True, False)
]

# Then asks the user questions until it narrows down which animal the user is thinking of
print("Think of an animal...")

remaining_choices = animal_list[:]
print(len(remaining_choices), "choices left")

possible_class_answers = []
for animal in animal_list:
    if animal.animal_class not in possible_class_answers:
        possible_class_answers.append(animal.animal_class)

possible_numlegs_answers = []
for animal in animal_list:
    if animal.num_legs not in possible_numlegs_answers:
        possible_numlegs_answers.append(animal.num_legs)
possible_numlegs_answers.sort()

possible_color_answers = []
for animal in animal_list:
    for color in animal.colors:
        if color not in possible_color_answers:
            possible_color_answers.append(color)

questions = ["class", "number of legs", "color", "feathers", "scales", "lays eggs", "flies"]

for question in questions:
    if question == "class":
        possible_answers = possible_class_answers
    elif question == "number of legs":
        possible_answers = possible_numlegs_answers
    elif question == "color":
        possible_answers = possible_color_answers
    else:
        possible_answers = ["True", "False"]

    user_input = input("What " + question + " is your animal?\nChoose from " + str(possible_answers) + "\nChoice: ")

    next_remaining_choice = []

    #filter list
    for animal in remaining_choices:
        if (question == "class" and user_input == animal.animal_class or
                question == "number of legs" and int(user_input) == animal.num_legs or
                question == "color" and user_input in animal.colors or
                question == "feathers" and user_input == str(animal.feathers) or
                question == "scales" and user_input == str(animal.scales) or
                question == "lays eggs" and user_input == str(animal.lays_eggs) or
                question == "flies" and user_input == str(animal.flies)):
            next_remaining_choice.append(animal)
    remaining_choices = next_remaining_choice
    print(len(remaining_choices), "choices left")

    if len(remaining_choices) == 1:
        user_input = input("Are you thinking of a " + remaining_choices[0].name.lower() + " (Y/N)? ")
        if user_input == "Y":
            print("Winner, winner, " + remaining_choices[0].name.lower() + " dinner!")
            break
        else:
            del remaining_choices[0]

    if len(remaining_choices) == 0:
        print("Your animal is not on our list.")
        break

print([str(a) for a in remaining_choices])
