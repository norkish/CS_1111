class Animal:
    def __init__(self, _name, _class, _num_legs, _colors, _feathers, _scales, _lays_eggs, _flies):
        self.name = _name
        self.animal_class = _class
        self.num_legs = _num_legs
        self.colors = _colors
        self.feathers = _feathers
        self.scales = _scales
        self.lays_eggs = _lays_eggs
        self.flies = _flies

    def __str__(self):
        return self.name
