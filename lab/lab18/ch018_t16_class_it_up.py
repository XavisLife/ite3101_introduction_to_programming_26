class Triangle(object):
    number_of_sides = 3

       def __init__(self, angle1: int, angle2: int, angle3: int):
            self.angle1 = angle1
            self.angle2 = angle2
            self.angle3 = angle3

        def check_angles(self):
            if (angle1 == 180 or angle2 == 180 or angle3 == 180):
                return True
            return False
