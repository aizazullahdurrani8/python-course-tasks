import math

class Shape:

    def __init__(self, name):
        self.name = name

    def area(self):
        print('Shape area')


class Rectangle(Shape):

    def __init__(self, len, bre):
        super().__init__('Rectangle')  # Optional: call parent constructor
        self.length = len
        self.breadth = bre

    def area(self):
        return self.length * self.breadth


class Circle(Shape):

    def __init__(self, rad):
        super().__init__('Circle')  # Optional: call parent constructor
        self.radius = rad

    def area(self):
        return math.pi * (self.radius ** 2)


r = Rectangle(10, 7)
print('Area:', r.area())