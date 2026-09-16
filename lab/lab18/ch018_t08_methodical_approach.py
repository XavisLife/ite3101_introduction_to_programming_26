class Animal(object):
    """Makes cute animals."""
    is_alive = True

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
    # Add your method here!
    def description(self, name, age):
        print(self.name)
        print(self.age)

hippo = Animal("Hippo", 6)
hippo.description