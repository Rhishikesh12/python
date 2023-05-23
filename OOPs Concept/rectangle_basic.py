class Rectangle:
    def __init__(self, width, height):
        # Initialize the attributes here
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
        

    def perimeter(self):
        return 2 * (self.width + self.height)

    def is_square(self):
        return self.width == self.height

rec = Rectangle(4,4)
print('Area of Rectangle :', rec.area())
print('Perimeter of Rectangle :', rec.perimeter())
print('is_Square :', rec.is_square(),'\n')


rec2 = Rectangle(5,4)
print('Area of Rectangle :', rec2.area())
print('Perimeter of Rectangle :', rec2.perimeter())
print('is_Square :', rec2.is_square())