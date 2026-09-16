class Car(object):

    def __init__(self, model: str, color: str, mpg: int):
        self.condition = "new"
        self.model = model
        self.color = color
        self.mpg = mpg

    def display_car

my_car = Car("DeLorean", "silver", 88)

print(my_car.model)
print(my_car.color)
print(my_car.mpg)
