square = lambda a: a * a
rectangle = lambda l, b: l * b
triangle = lambda b, h: 0.5 * b * h

a = int(input("Enter side of square: "))
print("Area of square:", square(a))

l = int(input("Enter length of rectangle: "))
b = int(input("Enter breadth of rectangle: "))
print("Area of rectangle:", rectangle(l, b))

b = int(input("Enter base of triangle: "))
h = int(input("Enter height of triangle: "))
print("Area of triangle:", triangle(b, h))
