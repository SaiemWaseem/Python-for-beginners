# super function: Function used to give the access to the method of the parent class. And return the temporary class object.

class Rectangles:
    def __init__(self,length,width):
        self.length = length
        self.width = width
class Square(Rectangles):
    def __init__(self,length,width):
        super().__init__(length,width)
    def area(self):
        return self.length*self.width

class Cube(Rectangles):
    def __init__(self,length,width,height):
        super().__init__(length,width)
        self.height = height
    def Volume(self):
        return self.length*self.width*self.height


Square = Square(3,3)
Cube = Cube(3,2,1)
print(Square.area())
print(Cube.Volume())
