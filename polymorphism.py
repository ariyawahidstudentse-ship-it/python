class square:

    def __init__ (self,side):
        self.side = side

    def area(self):
        print("My area is", self.side * self.side)

class circle:

    def __init__ (self,radius):
        self.radius = radius

    def area(self):
        print("My area is", 3.14 * self.radius * self.radius)

s = square(5)
c = circle(5)

for shape in (s,c):
    shape.area()
