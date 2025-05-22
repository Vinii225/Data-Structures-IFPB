# Exercise: Rectangle class with area calculation and square check.

class Rectangle:
    def __init__(self, height, base):
        self.__height=height
        self.__base=base

    def getHeight(self):
        return self.__height
    
    def getBase(self):
        return self.__base
    
    def calculateArea(self):
        return self.__base * self.__height
    
    def isSquare(self):
        if self.__base == self.__height:
            return True
        else:
            return False
        
    def __str__(self):
        return f"\nRectangle attributes:\nHeight: {self.getHeight()}\nBase: {self.getBase()}"


rectangle1 = Rectangle(5, 4)
print(rectangle1)
print(rectangle1.calculateArea())
print(rectangle1.isSquare())

rectangle2 = Rectangle(5, 5)
print(rectangle2)
print(rectangle2.calculateArea())
print(rectangle2.isSquare())