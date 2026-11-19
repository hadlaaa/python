from abc import ABC, abstractmethod

class Polygon(ABC):
    @abstractmethod
    def area(self):
        pass


class Rectangle(Polygon):
    def getdata(self):
        self.l = float(input("Enter length: "))
        self.b = float(input("Enter breadth: "))

    def area(self):
        print("Area of Rectangle:", self.l * self.b)


class Triangle(Polygon):
    def getdata(self):
        self.b = float(input("Enter base: "))
        self.h = float(input("Enter height: "))

    def area(self):
        print("Area of Triangle:", 0.5 * self.b * self.h)


r = Rectangle()
r.getdata()
r.area()

t = Triangle()
t.getdata()
t.area()
