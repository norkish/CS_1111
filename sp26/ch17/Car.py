class Car:
    def __init__(self, _make, _model, _fuel_type):
        self.color = None
        self.make = _make
        self.model = _model
        self.fuel_type = _fuel_type
        self.odometer_reading = 0

    def paint(self, _color):
        self.color = _color
