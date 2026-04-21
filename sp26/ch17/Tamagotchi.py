class Tamagotchi:
    def __init__(self, _name):
        self.name = _name
        self.happiness = 10     # scale of 1 to 10 (10 being happy)
        self.hunger = 0         # scale of 1 to 10 (10 being hungry)
        self.age = 0
        self.leg_lengths = [4,5,4,4]

    def get_hungry(self):
        self.hunger += 1

    def eat(self):
        self.hunger = 0
