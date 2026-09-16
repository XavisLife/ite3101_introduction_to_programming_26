class Car(object):

    def __init__(self, model: str, color: str, mpg: int):
        self.condition = "new"
        self.model = model
        self.color = color
        self.mpg = mpg

    def display_car(self):
        mpg_string = str(self.mpg))
        return f"This is a {self.color} {self.model} with {mpg_string} MPG."

my_car = Car("DeLorean", "silver", 88)

print(my_car.display_car)
