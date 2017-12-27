import math

class Circle:

    def __init__(self, radius):
        self.radius = radius  # the scope of 'radius' is limited to this __init__ method

    def get_area(self):
        return math.pi * self.radius ** 2

    def get_perimeter(self):
        return math.pi *2 * self.radius

    
