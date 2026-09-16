class Car(object):

    def __init__(self, model: str, color: str, mpg: int):
        self.condition = "new"
        self.model = model
        self.color = color
        self.mpg = mpg

    def display_car(self):
        print("This is a % s % swith % s MPG." %
              (self.color, self.model, str(self.mpg)))

    def drive_car(self):
        self.condition = "used"


class ElectricCar(Car):
    def __init__(self, battery_type, model, color, mpg):
        self.condition = super
        self.battery_type = battery_type
        self.model = model
        self.color = color
        self.mpg = mpg


my_car = ElectricCar("molten salt", "LX540", "blue", 88)
