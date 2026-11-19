# Import modules
from graphics import rectangle, circle
from graphics.threeD_graphics import cuboid, sphere

# Rectangle
l = float(input("Enter rectangle length: "))
b = float(input("Enter rectangle breadth: "))
print("Rectangle Area:", rectangle.area(l, b))
print("Rectangle Perimeter:", rectangle.perimeter(l, b))

# Circle
r = float(input("Enter circle radius: "))
print("Circle Area:", circle.area(r))
print("Circle Perimeter:", circle.perimeter(r))

# Cuboid
l = float(input("Enter cuboid length: "))
b = float(input("Enter cuboid breadth: "))
h = float(input("Enter cuboid height: "))
print("Cuboid Area:", cuboid.area(l, b, h))
print("Cuboid Perimeter:", cuboid.perimeter(l, b, h))

# Sphere
r = float(input("Enter sphere radius: "))
print("Sphere Area:", sphere.area(r))
print("Sphere Perimeter:", sphere.perimeter(r))
