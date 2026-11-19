class Rectangle:
    def getdata(self):
        self.length = float(input("Enter length: "))
        self.breadth = float(input("Enter breadth: "))

    def area(self):
        return self.length * self.breadth

    def perimeter(self):
        return 2 * (self.length + self.breadth)


r1 = Rectangle()
print("Enter First Rectangle Details")
r1.getdata()

r2 = Rectangle()
print("Enter Second Rectangle Details")
r2.getdata()

print("Area of First Rectangle:", r1.area())
print("Perimeter of First Rectangle:", r1.perimeter())

print("Area of Second Rectangle:", r2.area())
print("Perimeter of Second Rectangle:", r2.perimeter())

if r1.area() > r2.area():
    print("First Rectangle has greater area")
elif r1.area() < r2.area():
    print("Second Rectangle has greater area")
else:
    print("Both Rectangles have equal area")
