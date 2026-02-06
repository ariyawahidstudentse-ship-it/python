class square:
    def __init__ (self):
        self.__side = 10

    def area(self):
        print("side :", self.__side)
        print("My area is", self.__side**2)

s = square()
s.__side = 15
s.area()
